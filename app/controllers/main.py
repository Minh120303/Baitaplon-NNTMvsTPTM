import os
from flask import Blueprint, render_template, request, jsonify, current_app
from markupsafe import Markup
from werkzeug.utils import secure_filename
from app.models.leaf_predictor import LeafPredictor
from app.models.mongo_service import MongoService
from app.models.gemini_service import GeminiService

main_bp = Blueprint('main', __name__)
predictor = LeafPredictor()
mongo_service = MongoService()
gemini_service = GeminiService()

def allowed_file(filename):
    """Check if the file extension is allowed"""
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            result = predictor.predict(file)
            print(f"Prediction result: {result}") 
            
            if result['success']:
                label_parts = result['label'].split('___')
                plant_name = label_parts[0].replace('_', ' ').title()
                disease = label_parts[1].replace('_', ' ').title() if len(label_parts) > 1 else 'Healthy'
                
                treatment_result = gemini_service.get_treatment_recommendation(plant_name, disease)
                
                response_data = {
                    'label': result['label'],
                    'confidence': f"{result['confidence']*100:.2f}%",
                    'treatment': Markup(treatment_result['treatment']) if treatment_result['success'] else "Không thể tạo khuyến nghị điều trị."
                }
                
                prediction_id = mongo_service.save_prediction(filename, {
                    **result,
                    'treatment': treatment_result['treatment'] if treatment_result['success'] else None
                })
                
                if prediction_id:
                    response_data['prediction_id'] = prediction_id
                
                print(f"Sending response: {response_data}")  
                return jsonify(response_data)
            else:
                return jsonify({'error': result['error']}), 500
        else:
            return jsonify({'error': 'Invalid file type'}), 400

    page = request.args.get('page', 1, type=int)
    
    pagination_data = mongo_service.get_paginated_predictions(page)
    return render_template('index.html', **pagination_data)

@main_bp.route('/predictions', methods=['GET'])
def get_predictions():
    """API endpoint to get paginated predictions"""
    page = request.args.get('page', 1, type=int)
    return jsonify(mongo_service.get_paginated_predictions(page)) 