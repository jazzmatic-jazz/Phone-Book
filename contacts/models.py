from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contacts(models.Model):
    first_name = models.CharField(max_length=15, help_text="John")
    last_name = models.CharField(max_length=15, help_text="Doe")
    ph_num = PhoneNumberField()

    class Meta:
        ordering = ['first_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.ph_num}"