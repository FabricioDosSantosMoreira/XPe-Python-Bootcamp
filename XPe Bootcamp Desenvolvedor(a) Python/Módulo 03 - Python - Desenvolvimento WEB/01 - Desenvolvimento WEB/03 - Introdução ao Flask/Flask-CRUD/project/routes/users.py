from flask import Blueprint
from project.controllers.user import destroy, index, show, store, update

user_bp = Blueprint("user_bp", __name__)

user_bp.route("/", methods=["GET"])(index)
user_bp.route("/create", methods=["POST"])(store)
user_bp.route("/<int:user_id>", methods=["GET"])(show)
user_bp.route("/update/<int:user_id>", methods=["PUT"])(update)
user_bp.route("/delete/<int:user_id>", methods=["DELETE"])(destroy)
