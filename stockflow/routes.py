from flask import request, jsonify
from sqlalchemy import func
from datetime import datetime, timedelta
from stockflow import app, db
from stockflow.models import Product, Inventory, Supplier, InventoryChange, Warehouse

@app.route('/api/companies/<int:company_id>/alerts/low-stock', methods=['GET'])
def low_stock_alerts(company_id):
    recent_window = datetime.utcnow() - timedelta(days=30)

    subquery = db.session.query(
        InventoryChange.product_id
    ).join(Warehouse, Warehouse.id == InventoryChange.warehouse_id
    ).filter(
        InventoryChange.change_type == 'SALE',
        InventoryChange.timestamp >= recent_window,
        Warehouse.company_id == company_id
    ).distinct().subquery()

    results = db.session.query(
        Product.id.label("product_id"),
        Product.name.label("product_name"),
        Product.sku,
        Warehouse.id.label("warehouse_id"),
        Warehouse.name.label("warehouse_name"),
        Inventory.quantity.label("current_stock"),
        Product.threshold,
        func.avg(InventoryChange.quantity).label("avg_daily_sales")
    ).join(
        Inventory, Inventory.product_id == Product.id
    ).join(
        Warehouse, Inventory.warehouse_id == Warehouse.id
    ).join(
        InventoryChange, (InventoryChange.product_id == Product.id) &
                         (InventoryChange.change_type == 'SALE') &
                         (InventoryChange.timestamp >= recent_window)
    ).filter(
        Product.id.in_(subquery),
        Warehouse.company_id == company_id,
        Inventory.quantity < Product.threshold
    ).group_by(
        Product.id, Warehouse.id
    ).all()

    alerts = []
    for row in results:
        daily_avg = row.avg_daily_sales / 30 if row.avg_daily_sales else None
        days_until_stockout = int(row.current_stock / daily_avg) if daily_avg else None

        alerts.append({
            "product_id": row.product_id,
            "product_name": row.product_name,
            "sku": row.sku,
            "warehouse_id": row.warehouse_id,
            "warehouse_name": row.warehouse_name,
            "current_stock": row.current_stock,
            "threshold": row.threshold,
            "days_until_stockout": days_until_stockout
        })

    return jsonify({
        "alerts": alerts,
        "total_alerts": len(alerts)
    }), 200
