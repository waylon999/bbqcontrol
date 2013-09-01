from django.db import models

class Bbq(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
