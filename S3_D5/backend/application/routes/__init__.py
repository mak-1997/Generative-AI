from flask import Blueprint


# Create the Blueprint objects for each set of routes
dish_routes = Blueprint('dish_routes', __name__, url_prefix='/dishes')
user_routes = Blueprint('user_routes', __name__, url_prefix='/users')
admin_routes = Blueprint('admin_routes', __name__, url_prefix='/admins')
order_routes = Blueprint('order_routes', __name__, url_prefix='/orders')

# Import the route handlers from their respective files
from application.routes.dish_routes import *
from application.routes.user_routes import *
from application.routes.admin_routes import *
from application.routes.order_routes import *
