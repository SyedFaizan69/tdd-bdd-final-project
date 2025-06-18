def test_list_all_products(self):
    """Test listing all products"""
    for _ in range(3):
        product = ProductFactory()
        product.create()
    results = Product.all()
    self.assertEqual(len(results), 3)
