from django.db import models

class SavePost(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    nash_user = models.ForeignKey("NashUser", on_delete=models.CASCADE)