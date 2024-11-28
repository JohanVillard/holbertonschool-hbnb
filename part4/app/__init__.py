from flask import Flask, render_template
from flask_cors import CORS
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from app.routes.home import home_bp
from app.routes.login import login_bp
from app.routes.place import place_bp

# Instanciate the extensions
bcrypt = Bcrypt()
jwt = JWTManager()
db = SQLAlchemy()

from app.api.v1.users import api as users_api
from app.api.v1.places import api as places_api
from app.api.v1.amenities import api as amenities_api
from app.api.v1.reviews import api as reviews_api
from app.api.v1.auth import api as auth_api
from app.api.v1.admin import api as admin_api


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)

    # CORS for origin's authorizations
    CORS(app, supports_credentials=True, resources={
        r"/api/*": {
            "origins": [
                "http://127.0.0.1:5000", 
                "http://localhost:5000",
                "*"  # Autoriser toutes les origines en développement
            ],
            "allow_headers": [
                "Content-Type",
                "Authorization",
                "Access-Control-Allow-Credentials"
            ],
            "supports_credentials": True,
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
        }
    }) 

    # Load the configuration
    app.config.from_object(config_class)

    # Initialize of API Flask-RestX
    api = Api(app,
              version="1.0",
              title="HBnB API",
              description="HBnB Application API",
              doc='/api/docs',
              prefix='/api/v1')

    #  Add namespaces for API
    api.add_namespace(users_api)
    api.add_namespace(places_api)
    api.add_namespace(amenities_api)
    api.add_namespace(reviews_api)
    api.add_namespace(auth_api)
    api.add_namespace(admin_api)

    # Register the blueprints
    app.register_blueprint(home_bp) 
    app.register_blueprint(login_bp) 
    app.register_blueprint(place_bp) 

    # Initialize the extensions
    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    return app
