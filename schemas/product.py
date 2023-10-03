from models.product import Product
from extensions import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        sqla_session = db.session
        load_instance = True
        ordered = True
