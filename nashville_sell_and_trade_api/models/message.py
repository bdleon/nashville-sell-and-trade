from django.db import models

class Message(models.Model):
    recipient = models.ForeignKey("NashUser", on_delete=models.CASCADE, related_name="recieved_messages")
    sender = models.ForeignKey("NashUser", on_delete=models.CASCADE, related_name="sent_messages")
    message = models.TextField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)