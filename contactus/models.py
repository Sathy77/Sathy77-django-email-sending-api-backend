from django.db import models

class Contactus(models.Model):
    companyName = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    corporateEmail = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    protectDataByNDA = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.phone}'