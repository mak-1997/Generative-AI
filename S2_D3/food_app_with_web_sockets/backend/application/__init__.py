from flask import Flask
from flask_pymongo import PyMongo
from mongoengine import connect
from flask_bcrypt import Bcrypt  # Import Bcrypt
from application.converters import ObjectIdConverter
from application.routes.dish_routes import dish_routes
from application.routes.user_routes import user_routes
from application.routes.admin_routes import admin_routes
from application.routes.order_routes import order_routes
from flask_cors import CORS

# Create Flask app
app = Flask(__name__)
CORS(app)
app.url_map.converters['ObjectId'] = ObjectIdConverter

# Register the blueprints
app.register_blueprint(dish_routes)
app.register_blueprint(user_routes)
app.register_blueprint(admin_routes)
app.register_blueprint(order_routes)

# MongoDB connection
app.config["MONGO_URI"] = "mongodb+srv://mayank:singh@cluster0.3rdyhgg.mongodb.net/all_data?retryWrites=true&w=majority"
mongo = PyMongo(app)
db = mongo.db

# Initialize Bcrypt
bcrypt = Bcrypt(app)


connect("all_data", host=app.config["MONGO_URI"])
