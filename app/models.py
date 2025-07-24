from . import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sku = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    threshold = db.Column(db.Integer, default=10)

class Warehouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

class Inventory(db.Model):
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouse.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    contact_email = db.Column(db.String)

class InventoryChange(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    warehouse_id = db.Column(db.Integer)
    change_type = db.Column(db.String)
    quantity = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
