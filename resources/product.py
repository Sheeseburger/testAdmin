from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import request, jsonify
from schemas.product import ProductSchema
from models.product import Product
from extensions import db

class ProductResource(Resource):
    @jwt_required()
    def get(self):
        criterias = {}
        offer_of_the_month = request.args.get('offer_of_the_month', default= -1)
        available = request.args.get('available', default=-1)
        self_pickup = request.args.get('self_pickup', default=-1)
        if offer_of_the_month != -1:
            criterias['offer_of_the_month'] = offer_of_the_month
        if available != -1:
            criterias['available'] = available
    
        if self_pickup != -1:
            criterias['self_pickup'] = self_pickup
        schema = ProductSchema(many=True)
        return {"products": schema.dump(Product.query.filter_by(**criterias).all())}
    
    def post(self):
        schema = ProductSchema()
        product = schema.load(request.json)

        db.session.add(product)
        db.session.commit()
        return {"message": "Product created", "product": schema.dump(product)}, 201
    def delete(self):
        product = Product.query.get_or_404(request.json)
        db.session.delete(product)
        db.session.commit()
        return {"message":"Product deleted"}
    def patch(self):
        product_id = request.json.get('id')
        if not product_id:
            return jsonify({"message": "Product ID is required"}), 400

        product = Product.query.filter_by(id=product_id).first()
        if not product:
            return jsonify({"message:":"No user with this id"}), 400
        updated_data = request.json.get('data')

        if not updated_data:
            return jsonify({"message": "Updated data is required"}), 400
        for key, value in updated_data.items():
            setattr(product, key, value)

        db.session.commit()
        return {"msg": "Product updated", "product": ProductSchema().dump(product)}
