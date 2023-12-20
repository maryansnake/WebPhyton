from flask import Blueprint

api_bp = Blueprint('api', __name__)

from .cars import api_cars_bp
api_bp.register_blueprint(api_cars_bp, url_prefix="/cars")

from . import controller