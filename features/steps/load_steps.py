from behave import given
import json
from service.models import db, Product, Category
from tests.factories import ProductFactory

@given('the following products')
def step_impl(context):
    """Load products into the database from the feature table"""
    db.session.query(Product).delete()
    db.session.commit()

    for row in context.table:
        product = Product(
            name=row['name'],
            description=row['description'],
            price=row['price'],
            available=row['available'].lower() == 'true',
            category=Category[row['category'].upper()]
        )
        product.create()
