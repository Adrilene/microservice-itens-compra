from flask import request, jsonify
from purchase_items.services.purchase_items_service import (
    get_purchase_items_by_user_id,
    get_purchase_items_by_user_agent,
    delete_item_by_item_id,
    insert_purchase_item,
    update_purchase_items_by_user_id,
)
from flask_restful import Resource
from purchase_items import app, api
import json
import io




class PurchaseItemItemIDController(Resource):
    def delete(self, item_id):
        purchase_items = delete_item_by_item_id(item_id)
        return "OK", 200


class PurchaseItemUserIDController(Resource):
    def get(self, user_id):
        purchase_items = get_purchase_items_by_user_id(user_id)
        purchase_items = json.loads(purchase_items.to_json())
        return purchase_items, 200


class PurchaseItemController(Resource):
    def get(self):
        purchase_items = get_purchase_items_by_user_agent(
            request.headers.get("User-Agent")
        )
        purchase_items = json.loads(purchase_items.to_json())
        return purchase_items, 200

    def post(self):
        data_json = {
            "product_id": request.json["_id"],
            "user_agent": request.headers.get("User-Agent"),
        }
        insert_purchase_item(data_json)
        return "OK", 200

    def put(self):
        user_agent = request.headers.get("User-Agent")
        purchase_items = update_purchase_items_by_user_id(
            user_agent, request.json["subtotal"]
        )
        return {"msg" "ok"}, 200


# api.add_resource(PurchaseItemUserAgentController, "/purchase_item/<user_agent>")

api.add_resource(PurchaseItemItemIDController, "/purchase_item/item/<item_id>")
api.add_resource(PurchaseItemUserIDController, "/purchase_item/user/<user_id>")
api.add_resource(PurchaseItemController, "/purchase_item")
