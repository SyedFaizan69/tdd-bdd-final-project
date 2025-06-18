import unittest
from service.models import db, Product, Category
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Initialize the database once for all tests"""
        from service.models import init_db
        from app import app  # Make sure this exists in your project
        init_db(app)

    def setUp(self):
        """Reset the database before each test"""
        db.session.query(Product).delete()
        db.session.commit()

    def test_read_product(self):
        """Test reading a product from the database"""
        product = ProductFactory()
        product.create()
        found = Product.find(product.id)
        self.assertIsNotNone(found)
        self.assertEqual(found.id, product.id)

    def test_update_product(self):
        """Test updating a product"""
        product = ProductFactory()
        product.create()
        product.name = "UpdatedName"
        product.update()
        updated = Product.find(product.id)
        self.assertEqual(updated.name, "UpdatedName")

    def test_delete_product(self):
        """Test deleting a product"""
        product = ProductFactory()
        product.create()
        product_id = product.id
        product.delete()
        result = Product.find(product_id)
        self.assertIsNone(result)

    def test_list_all_products(self):
        """Test listing all products"""
        for _ in range(3):
            product = ProductFactory()
            product.create()
        results = Product.all()
        self.assertEqual(len(results), 3)

    def test_find_by_name(self):
        """Test finding products by name"""
        product = ProductFactory(name="Wrench")
        product.create()
        results = Product.find_by_name("Wrench").all()
        self.assertGreaterEqual(len(results), 1)
        self.assertEqual(results[0].name, "Wrench")

    def test_find_by_category(self):
        """Test finding products by category"""
        product = ProductFactory(category=Category.TOOLS)
        product.create()
        results = Product.find_by_category(Category.TOOLS).all()
        self.assertGreaterEqual(len(results), 1)
        self.assertEqual(results[0].category, Category.TOOLS)

    def test_find_by_availability(self):
        """Test finding products by availability"""
        product = ProductFactory(available=True)
        product.create()
        results = Product.find_by_availability(True).all()
        self.assertGreaterEqual(len(results), 1)
        self.assertTrue(results[0].available)
