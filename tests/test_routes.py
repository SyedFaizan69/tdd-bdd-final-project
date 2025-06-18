import unittest
import json
from service.models import db, Product, Category
from service import app
from tests.factories import ProductFactory

class TestProductRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        db.session.query(Product).delete()
        db.session.commit()

    def _create_product(self):
        """Helper method to create and return a product"""
        product = ProductFactory()
        product.create()
        return product

    def test_read_product(self):  # 3a
        product = self._create_product()
        response = self.client.get(f"/products/{product.id}")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["id"], product.id)

    def test_update_product(self):  # 3b
        product = self._create_product()
        updated_data = product.serialize()
        updated_data["name"] = "UpdatedProduct"
        response = self.client.put(
            f"/products/{product.id}",
            json=updated_data,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["name"], "UpdatedProduct")

    def test_delete_product(self):  # 3c
        product = self._create_product()
        response = self.client.delete(f"/products/{product.id}")
        self.assertEqual(response.status_code, 204)

        # Confirm it's gone
        get_response = self.client.get(f"/products/{product.id}")
        self.assertEqual(get_response.status_code, 404)

    def test_list_all_products(self):  # 3d
        for _ in range(3):
            self._create_product()
        response = self.client.get("/products")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 3)

    def test_list_by_name(self):  # 3e
        product = ProductFactory(name="Drill")
        product.create()
        response = self.client.get("/products", query_string={"name": "Drill"})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data[0]["name"], "Drill")

    def test_list_by_category(self):  # 3f
        product = ProductFactory(category=Category.FOOD)
        product.create()
        response = self.client.get("/products", query_string={"category": "FOOD"})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data[0]["category"], "FOOD")

    def test_list_by_availability(self):  # 3g
        product = ProductFactory(available=True)
        product.create()
        response = self.client.get("/products", query_string={"available": "true"})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data[0]["available"])
