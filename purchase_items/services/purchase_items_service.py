from purchase_items.models.purchase_items_model import PurchaseItems
import requests


def get_purchase_items(user_id):
    return PurchaseItems.objects(user_id=user_id)


def insert_purchase_item(body: dict):
    data_product = requests.get(f"http://localhost:5005/product/{body['product_id']}").json()
    data = {
        "name": data_product["name"],
        "price": data_product["price"] - data_product["discount_price"]
        if data_product["discount"]
        else data_product["price"],
        "product_id": body["product_id"],
        "user_id": body["user_id"],
    }
    purchase_item = PurchaseItems(**data)
    purchase_item.save()
    return str(purchase_item.id)
