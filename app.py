import os
from flask import Flask, render_template
from flask_restful import Api
from flask_jwt_extended import JWTManager


from extensions import db, migrate
from resources.product import ProductResource
from resources.login import LoginResource
from data.testdata import create_default_data
def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
   
    set_extensions(app)
    api.add_resource(ProductResource, '/')
    api.add_resource(LoginResource, '/login')
    # @app.route('/login', methods=['GET'])
    # def login():
    #     return render_template('login.html')
    return app

def set_extensions(app):
    JWTManager(app)
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        try:
            print('starting creating')
            if os.getenv('CREATE_DEFAULT_DATA'):
                create_default_data()
        except Exception as e:
            print(e)
   

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
  
