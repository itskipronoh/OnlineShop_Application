# from django.db import models
#
# # cCreate your models here.
# class Customer(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     phone = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#     age = models.IntegerField(null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#
#     def __str__(self):
#         return self.name, self.phone, self.email,self.age, self.date_created

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.IntegerField()
    admNo = models.CharField(max_length=10)

    def __str__(self):
        return self.name


def validate_age():
    return None


def age_validator():
    return None
