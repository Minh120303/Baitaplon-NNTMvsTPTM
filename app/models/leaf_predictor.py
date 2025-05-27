import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import json
import os
from io import BytesIO

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 0 = ALL, 1 = INFO, 2 = WARNING, 3 = ERROR

class LeafPredictor:
    def __init__(self):
        self.model = None
        self.class_labels = None
        self._load_model()
        self._load_labels()

    def _load_model(self):
        model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'last.h5')
        self.model = load_model(model_path)

    def _load_labels(self):
        labels_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'class_labels_vi.json')
        try:
            with open(labels_path, 'r', encoding='utf-8') as f:
                self.class_labels = json.load(f)
        except Exception as e:
            print(f"Error loading class labels: {str(e)}")
            raise

    def preprocess_image(self, file_storage):
        img_bytes = BytesIO(file_storage.read())
        file_storage.seek(0)
        
        img = image.load_img(img_bytes, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = img_array / 255.0
        return np.expand_dims(img_array, axis=0)

    def predict(self, file_storage):
        try:
            processed_image = self.preprocess_image(file_storage)
            
            prediction = self.model.predict(processed_image)
            predicted_index = np.argmax(prediction)
            predicted_label = self.class_labels[predicted_index]
            confidence = float(prediction[0][predicted_index])
            
            return {
                'success': True,
                'label': predicted_label,
                'confidence': confidence,
                'error': None
            }
        except Exception as e:
            return {
                'success': False,
                'label': None,
                'confidence': None,
                'error': str(e)
            } 