from django.db import models

# Create your models here.
class Member(models.Model):
    Name=models.CharField(max_length=50)
    Password=models.CharField(max_length=12)
    Email=models.EmailField(max_length=256)

    def __str__(self):
        return self.Name + " " + self.Email