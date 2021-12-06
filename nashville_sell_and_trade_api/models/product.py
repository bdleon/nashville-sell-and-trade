from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    categories = models.ManyToManyField("Category", through="ProductCategory", related_name="products")
    price = models.IntegerField()
    image = models.CharField(max_length=150)
    trade = models.BooleanField()
    quantity = models.IntegerField()
    nash_user = models.ForeignKey("NashUser", on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)