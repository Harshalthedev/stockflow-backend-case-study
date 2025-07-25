# init_db.py
from stockflow import app, db
from stockflow.models import Company, Warehouse

with app.app_context():
    db.drop_all()
    db.create_all()

    demo_company = Company(id=1, name='Demo Company')
    main_warehouse = Warehouse(id=1, name='Main Warehouse', company_id=1)

    db.session.add_all([demo_company, main_warehouse])
    db.session.commit()

    print("✅ Tables dropped, recreated, and demo data inserted!")
