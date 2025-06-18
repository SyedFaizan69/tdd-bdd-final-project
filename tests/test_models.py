def test_find_by_name(self):
    """Test finding products by name"""
    product = ProductFactory(name="Wrench")
    product.create()
    results = Product.find_by_name("Wrench").all()
    self.assertGreaterEqual(len(results), 1)
    self.assertEqual(results[0].name, "Wrench")
