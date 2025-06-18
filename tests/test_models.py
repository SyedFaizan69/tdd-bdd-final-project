def test_delete_product(self):
    """Test deleting a product"""
    product = ProductFactory()
    product.create()
    product_id = product.id
    product.delete()
    result = Product.find(product_id)
    self.assertIsNone(result)
