from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token
from flask import request,jsonify
from models.user import User
from passlib.hash import sha256_crypt 

class LoginResource(Resource):
    @jwt_required()    
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        if not username or not password:
            return jsonify({"message": "Invalid credentials"}), 401
        user = User.query.filter_by(username=username).first()
        if user and sha256_crypt.verify(password, user.password):
            access_token = create_access_token(identity=user.id)
            return jsonify({"access_token": access_token}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401
   