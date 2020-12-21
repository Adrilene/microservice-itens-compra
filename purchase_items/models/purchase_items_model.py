from purchase_items import db
from datetime import datetime


class Item(db.EmbeddedDocument):
    name = db.StringField(required=True)
    id = db.StringField(required=True)
    price = db.FloatField(required=True)
    qtd = db.IntField(1, required=False)


class PurchaseItems(db.Document):
    meta = {"collection": "purchase-items"}
    subtotal = db.FloatField(required=False)
    total = db.FloatField(required=False)
    user_id = db.StringField(required=False)
    user_agent = db.StringField(required=False)
    itens = db.EmbeddedDocumentListField(Item, required=False)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)
