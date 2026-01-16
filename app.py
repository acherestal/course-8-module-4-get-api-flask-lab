from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """Homepage route: simple welcome message."""
    return jsonify({"message": "Welcome to the Product Catalog API!"}), 200


@app.route("/products", methods=["GET"])
def get_products():
    """Return all products, optionally filtered by category via ?category=."""
    category = request.args.get("category")
    if category:
        category_norm = category.strip().lower()
        filtered = [
            p for p in products
            if str(p.get("category", "")).lower() == category_norm
        ]
        return jsonify(filtered), 200

    return jsonify(products), 200


@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id: int):
    """Return a single product by id, or a 404 JSON error."""
    product = next((p for p in products if p.get("id") == id), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200


if __name__ == "__main__":
    app.run(debug=True)
