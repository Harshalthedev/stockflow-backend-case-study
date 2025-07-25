# 📦 StockFlow — Backend Engineering Case Study

![Flask](https://img.shields.io/badge/built%20with-Flask-blue.svg)
![PostgreSQL](https://img.shields.io/badge/database-PostgreSQL-informational)
![Status](https://img.shields.io/badge/status-ready--to--submit-brightgreen)

> This repository contains my solution for the **Backend Engineering Intern Case Study** for a B2B Inventory Management SaaS platform: **StockFlow**.

---

## 🚀 Project Overview

StockFlow is an internal backend system for managing:
- Inventory across multiple warehouses
- Supplier relationships
- Product bundles
- Low-stock alerts

The case study is divided into 3 key parts:
1. Code Review & Debugging
2. Database Design
3. Low-Stock Alert API Implementation

---

## 🧩 Part 1: Code Review & Fixes

- Reviewed a broken `POST /api/products` endpoint
- Identified bugs and business logic flaws
- Implemented fixes for:
  - SKU uniqueness
  - Safe Decimal pricing
  - Transaction handling
  - Field validation

> ✅ Full implementation in `app/routes.py`  
> 🧠 Reasoning in `case_study_report.md`

---

## 🗃️ Part 2: Database Schema

Key entities:
- `Products`, `Warehouses`, `Inventory`
- `Suppliers`, `InventoryChanges`, `ProductBundles`

Implemented as normalized schema in `schema.sql` with:
- Foreign keys
- Composite primary keys
- Many-to-many relationships
- Change tracking for alerts

---

## 🔔 Part 3: Low-Stock Alert API

### Endpoint

```http
GET /api/companies/{company_id}/alerts/low-stock
```

### Returns:

```json
{
  "alerts": [
    {
      "product_id": 123,
      "product_name": "Widget A",
      "sku": "WID-001",
      "warehouse_id": 456,
      "warehouse_name": "Main Warehouse",
      "current_stock": 5,
      "threshold": 20,
      "days_until_stockout": 12,
      "supplier": {
        "id": 789,
        "name": "Supplier Corp",
        "contact_email": "orders@supplier.com"
      }
    }
  ],
  "total_alerts": 1
}
```

- ✅ Filters for products with recent sales
- ✅ Shows supplier contact info
- ✅ Calculates `days_until_stockout` based on 30-day average sales

---

## 🛠 Setup & Run Locally

```bash
# Clone repo
git clone https://github.com/yourusername/stockflow-case-study.git
cd stockflow-case-study

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python run.py
```

---

## 📸 Screenshots

> Replace these with your own if needed

### ✅ Low Stock Alert Response
![Low Stock JSON](screenshots/low-stock-response.png)

### ✅ ERD Schema
![ERD Schema](screenshotserd-diagram.png)

---

## 📂 Project Structure

```
stockflow-case-study/
├── app/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── schema.sql
├── run.py
├── requirements.txt
├── case_study_report.md
└── README.md
```

---

## 📌 Assumptions Made

- “Recent sales activity” means sales in the past 30 days
- All thresholds are stored in the product table
- Days until stockout is estimated using average daily sales

See more in `case_study_report.md`

---

## 📞 Contact

Made with ❤️ by [Your Name]  
[GitHub](https://github.com/Harshalthedev) | [LinkedIn](https://linkedin.com/in/harshal-thakare-404835257/)

---

## 🧪 License

This project is licensed under the MIT License.
