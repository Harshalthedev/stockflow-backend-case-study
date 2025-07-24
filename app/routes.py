from flask import request, jsonify
from sqlalchemy import func
from datetime import datetime, timedelta
from . import app, db
from .models import Product, Inventory, Supplier, InventoryChange

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    required_fields = ['name', 'sku', 'price', 'warehouse_id', 'initial_quantity']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    if Product.query.filter_by(sku=data['sku']).first():
        return jsonify({"error": "SKU must be unique"}), 400

    try:
        from decimal import Decimal
        with db.session.begin():
            product = Product(
                name=data['name'],
                sku=data['sku'],
                price=Decimal(str(data['price']))
            )
            db.session.add(product)
            db.session.flush()

            inventory = Inventory(
                product_id=product.id,
                warehouse_id=data['warehouse_id'],
                quantity=data['initial_quantity']
            )
            db.session.add(inventory)

        return jsonify({"message": "Product created", "product_id": product.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
