from flask import Blueprint, request, jsonify, abort
from service.models import Product, Category

bp = Blueprint("products", __name__)

@bp.route("/products/<int:product_id>", methods=["GET"])  # Task 4a
def get_product(product_id):
    product = Product.find(product_id)
    if not product:
        abort(404, f"Product with id {product_id} not found.")
    return jsonify(product.serialize()), 200

@bp.route("/products/<int:product_id>", methods=["PUT"])  # Task 4b
def update_product(product_id):
    product = Product.find(product_id)
    if not product:
        abort(404, f"Product with id {product_id} not found.")
    data = request.get_json()
    product.deserialize(data)
    product.id = product_id  # ensure it doesn't get reset
    product.update()
    return jsonify(product.serialize()), 200

@bp.route("/products/<int:product_id>", methods=["DELETE"])  # Task 4c
def delete_product(product_id):
    product = Product.find(product_id)
    if not product:
        abort(404, f"Product with id {product_id} not found.")
    product.delete()
    return "", 204

@bp.route("/products", methods=["GET"])  # Task 4d
def list_products():
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")

    results = Product.all()

    if name:
        results = Product.find_by_name(name).all()
    elif category:
        try:
            cat_enum = Category[category.upper()]
            results = Product.find_by_category(cat_enum).all()
        except KeyError:
            abort(400, f"Invalid category: {category}")
    elif available:
        if available.lower() not in ["true", "false"]:
            abort(400, f"Invalid availability: {available}")
        is_available = available.lower() == "true"
        results = Product.find_by_availability(is_available).all()

    return jsonify([p.serialize() for p in results]), 200
