def test_read_product(self):
    """Test reading a product from the database"""
    product = ProductFactory()
    product.create()
    found = Product.find(product.id)
    self.assertIsNotNone(found)
    self.assertEqual(found.id, product.id)
