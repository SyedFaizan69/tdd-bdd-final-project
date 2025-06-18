def test_find_by_category(self):
    """Test finding products by category"""
    product = ProductFactory(category=Category.TOOLS)
    product.create()
    results = Product.find_by_category(Category.TOOLS).all()
    self.assertGreaterEqual(len(results), 1)
    self.assertEqual(results[0].category, Category.TOOLS)
