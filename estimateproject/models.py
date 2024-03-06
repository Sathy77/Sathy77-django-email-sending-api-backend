from django.db import models
from datetime import datetime

def getUniqueCodePattern():
    return f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}"[:18]
def directory_path(instance, filename):
    return f'pdf/{getUniqueCodePattern()}.pdf'

class Userdetails(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.email}'

class Estimateproject(models.Model):
    projectType = models.CharField(max_length=100, blank=True, null=True)
    yourRole = models.CharField(max_length=100, blank=True, null=True)
    # servicesNeeded = models.CharField(max_length=100, blank=True, null=True)
    preferredContactTime = models.CharField(max_length=100, blank=True, null=True)
    attachment = models.FileField(upload_to=directory_path, max_length=250, null=True, default=None)
    attachmentname = models.CharField(max_length=100, blank=True, null=True, editable=False)
    projectDetails = models.CharField(max_length=100, blank=True, null=True)
    userDetails = models.OneToOneField(Userdetails, on_delete=models.CASCADE)
    newsletterSubscription = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.projectType} - {self.yourRole} - {self.attachmentname}'
    def save(self, *args, **kwargs):
        self.attachmentname = str(self.attachment)
        super().save(*args, **kwargs)

class Challenge(models.Model):
    fieldName = models.CharField(max_length=100)
    value = models.BooleanField(default=True)
    estimateProject = models.ForeignKey(Estimateproject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fieldName} - {self.value}'

class Alreadyhave(models.Model):
    fieldName = models.CharField(max_length=100)
    value = models.BooleanField(default=True)
    estimateProject = models.ForeignKey(Estimateproject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fieldName} - {self.value}'

class Timeframe(models.Model):
    fieldName = models.CharField(max_length=100)
    value = models.BooleanField(default=True)
    estimateProject = models.ForeignKey(Estimateproject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fieldName} - {self.value}'