# seed_low_stock.py
from datetime import datetime, timedelta
from stockflow import app, db
from stockflow.models import Product, Inventory, InventoryChange
from decimal import Decimal

with app.app_context():
    # Create a product that's below threshold
    product = Product(
        name='Widget A',
        sku='WID-LOW',
        price=Decimal('49.99'),
        threshold=50  # Low threshold
    )
    db.session.add(product)
    db.session.flush()  # get product.id

    # Add current stock
    inventory = Inventory(
        product_id=product.id,
        warehouse_id=1,
        quantity=10  # Low stock to trigger alert
    )
    db.session.add(inventory)

    # Add recent sales activity (simulate past 5 days)
    now = datetime.utcnow()
    for i in range(1, 6):
        change = InventoryChange(
            product_id=product.id,
            warehouse_id=1,
            change_type='SALE',
            quantity=5,
            timestamp=now - timedelta(days=i)
        )
        db.session.add(change)

    db.session.commit()
    print("✅ Seeded product, inventory, and sales data for low-stock alert test.")
