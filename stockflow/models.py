from stockflow import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sku = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    threshold = db.Column(db.Integer, nullable=False, default=10)  # ✅ this line

class Warehouse(db.Model):
    __tablename__ = 'warehouses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class Inventory(db.Model):
    __tablename__ = 'inventory'
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouses.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

class Supplier(db.Model):
    __tablename__ = 'suppliers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    contact_email = db.Column(db.String)

class InventoryChange(db.Model):
    __tablename__ = 'inventory_changes'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    warehouse_id = db.Column(db.Integer)
    change_type = db.Column(db.String)
    quantity = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)