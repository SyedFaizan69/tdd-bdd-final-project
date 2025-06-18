def test_update_product(self):
    """Test updating a product"""
    product = ProductFactory()
    product.create()
    product.name = "UpdatedName"
    product.update()
    updated = Product.find(product.id)
    self.assertEqual(updated.name, "UpdatedName")
