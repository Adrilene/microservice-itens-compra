from purchase_items import db
from datetime import datetime


class PurchaseItems(db.Document):
    meta = {"collection": "purchase-items"}
    name = db.StringField(required=True)
    price = db.FloatField(required=True)
    product_id = db.StringField(required=True)
    user_id = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)
