from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name="Brand Name")
    mobile1 = models.CharField(max_length=15, null=True, blank=True, verbose_name="Mobile 1")
    mobile2 = models.CharField(max_length=15, null=True, blank=True, verbose_name="Mobile 2")
    email = models.EmailField(null=True, blank=True, verbose_name="Email ID")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name
