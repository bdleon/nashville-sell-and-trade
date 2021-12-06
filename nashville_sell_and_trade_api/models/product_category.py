from django.db import models

class ProductCategory(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)