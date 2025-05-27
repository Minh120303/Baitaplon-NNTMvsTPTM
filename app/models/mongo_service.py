from pymongo import MongoClient
from datetime import datetime
import os
from math import ceil
from bson import ObjectId, json_util    
import json

class MongoService:
    def __init__(self):
        mongo_uri = os.getenv('MONGODB_URI', 'mongodb+srv://leminh:leminh123@cluster0.4se7oyy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        self.client = MongoClient(mongo_uri)
        self.db = self.client['leaf_prediction']
        self.predictions = self.db['predictions']
        self.ITEMS_PER_PAGE = 5

    def save_prediction(self, image_filename, prediction_result):
        document = {
            'timestamp': datetime.utcnow(),
            'image_filename': image_filename,
            'predicted_label': prediction_result['label'],
            'confidence': prediction_result['confidence'],
            'treatment': prediction_result['treatment']
        }
        
        try:
            result = self.predictions.insert_one(document)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error saving to MongoDB: {str(e)}")
            return None

    def get_paginated_predictions(self, page=1):
        try:
            skip = (page - 1) * self.ITEMS_PER_PAGE

            total_items = self.predictions.count_documents({})
            total_pages = ceil(total_items / self.ITEMS_PER_PAGE)

            cursor = self.predictions.find() \
                        .sort('timestamp', -1) \
                        .skip(skip) \
                        .limit(self.ITEMS_PER_PAGE)
            
            predictions = []
            for doc in cursor:
                doc['_id'] = str(doc['_id'])
                doc['timestamp'] = doc['timestamp'].isoformat()
                predictions.append(doc)

            return {
                'predictions': predictions,
                'current_page': page,
                'total_pages': total_pages,
                'total_items': total_items,
                'has_prev': page > 1,
                'has_next': page < total_pages
            }
        except Exception as e:
            print(f"Error retrieving from MongoDB: {str(e)}")
            return {
                'predictions': [],
                'current_page': 1,
                'total_pages': 1,
                'total_items': 0,
                'has_prev': False,
                'has_next': False
            }

    def get_prediction_by_id(self, prediction_id):
        try:
            doc = self.predictions.find_one({'_id': ObjectId(prediction_id)})
            if doc:
                doc['_id'] = str(doc['_id'])
                doc['timestamp'] = doc['timestamp'].isoformat()
            return doc
        except Exception as e:
            print(f"Error retrieving prediction: {str(e)}")
            return None 