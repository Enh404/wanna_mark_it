from django.db import models

class Achievement(models.Model):
    name = models.CharField(max_length=200)
    requirement = models.CharField(max_length=200)
    ach_img = models.ImageField(null=True, blank=True, upload_to='ach/')

    def __str__(self):
        return self.name
