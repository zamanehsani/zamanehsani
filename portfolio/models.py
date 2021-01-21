from django.db import models

class Index(models.Model):
    first_name         = models.CharField(max_length=150, null=True, blank=True)
    last_name          = models.CharField(max_length=150, null=True, blank=True)
    position           = models.CharField(max_length=150, null=True, blank=True)
    company            = models.CharField(max_length=150, null=True, blank=True)
    email         = models.EmailField(null=True, blank=True)
    message      = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name