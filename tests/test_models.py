def test_find_by_availability(self):
    """Test finding products by availability"""
    product = ProductFactory(available=True)
    product.create()
    results = Product.find_by_availability(True).all()
    self.assertGreaterEqual(len(results), 1)
    self.assertTrue(results[0].available)
