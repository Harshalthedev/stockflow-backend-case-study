-- Companies
CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL
);

-- Warehouses
CREATE TABLE warehouses (
    id SERIAL PRIMARY KEY,
    company_id INT REFERENCES companies(id),
    name VARCHAR NOT NULL
);

-- Products
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    sku VARCHAR UNIQUE NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    threshold INT NOT NULL DEFAULT 10
);

-- Inventory
CREATE TABLE inventory (
    product_id INT REFERENCES products(id),
    warehouse_id INT REFERENCES warehouses(id),
    quantity INT NOT NULL,
    PRIMARY KEY (product_id, warehouse_id)
);

-- Suppliers
CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    contact_email VARCHAR
);

-- Product-Supplier Mapping
CREATE TABLE product_suppliers (
    product_id INT REFERENCES products(id),
    supplier_id INT REFERENCES suppliers(id),
    PRIMARY KEY (product_id, supplier_id)
);

-- Inventory Change Logs
CREATE TABLE inventory_changes (
    id SERIAL PRIMARY KEY,
    product_id INT,
    warehouse_id INT,
    change_type VARCHAR,
    quantity INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Bundles
CREATE TABLE product_bundles (
    bundle_id INT REFERENCES products(id),
    component_id INT REFERENCES products(id),
    quantity INT NOT NULL,
    PRIMARY KEY (bundle_id, component_id)
);
