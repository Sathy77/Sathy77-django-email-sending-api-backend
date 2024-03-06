from django.db import models

class Userdetails(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.phone}'
    
class Requestschedule(models.Model):
    service = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    time = models.CharField(max_length=20, blank=True, null=True)
    budget = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    userDetails = models.OneToOneField(Userdetails, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.service} - {self.date} - {self.date}'

class Budgetdetails(models.Model):
    budgetid = models.IntegerField()
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.budgetid} - {self.name}'
    