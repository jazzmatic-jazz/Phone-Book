from pyexpat import model
from django.db import models

class Contacts(models.Model):
    first_name = models.CharField(max_length=15, help_text="John")
    last_name = models.CharField(max_length=15, help_text="Doe")
    ph_num = models.CharField(max_length=10, help_text="9999999999")

    class Meta:
        ordering = ['-first_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.ph_num}"