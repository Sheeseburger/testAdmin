from models.user import User
from extensions import db, ma

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True
        ordered = True
