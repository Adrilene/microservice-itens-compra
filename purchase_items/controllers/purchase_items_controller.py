from flask import request, jsonify
from purchase_items.services.purchase_items_service import (
    get_purchase_items,
    insert_purchase_item,
)
from flask_restful import Resource
from purchase_items import app, api
import json
import io


class PurchaseItemIDController(Resource):
    def get(self, user_id):
        purchase_items = get_purchase_items(user_id)
        purchase_items = json.loads(purchase_items.to_json())
        return purchase_items, 200

    
class PurchaseItemController(Resource):   
    def post(self):
        data_json = {
            "product_id": request.form["product_id"],
            "user_id": request.form["user_id"],
        }
        insert_purchase_item(data_json)
        return 'OK', 200


api.add_resource(PurchaseItemIDController, "/purchase_item/<user_id>")
api.add_resource(PurchaseItemController, "/purchase_item")
