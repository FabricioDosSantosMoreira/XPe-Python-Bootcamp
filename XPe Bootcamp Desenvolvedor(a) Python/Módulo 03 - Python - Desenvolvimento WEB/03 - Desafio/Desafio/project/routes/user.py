from flask import Blueprint
from project.controllers.user import create, delete, index, update

user_bp = Blueprint("user_bp", __name__, url_prefix="/users")

user_bp.route("/", methods=["GET"])(index)
user_bp.route("/create", methods=["POST"])(create)
user_bp.route("/update/<int:user_id>", methods=["POST"])(update)
user_bp.route("/delete/<int:user_id>", methods=["POST"])(delete)
