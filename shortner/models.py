from django.db import models

class shorturl(models.Model):
    original_url = models.URLField(blank=False)
    short_url = models.URLField(blank=False)
    result = models.CharField(blank=False, max_length=100000)
    def __str__(self):
        return self.result
   
