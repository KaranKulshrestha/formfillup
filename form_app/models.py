from django.db import models

# Create your models here.

class Profile(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Profession = models.CharField(max_length=50)
    Salary = models.CharField(max_length=50)

    def __str__(self):
        return self.First_Name
    

class Contact(models.Model):
    First_Name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Phone_Numbers = models.IntegerField(max_length=13)

    def __int__(self):
        return self.Phone_Numbers

