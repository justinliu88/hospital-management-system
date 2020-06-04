from django.db import models

# Create your models here.

class Doct(models.Model):
    UID = models.AutoField(primary_key=True)
    Phone = models.CharField(max_length=20)
    eMail = models.EmailField(max_length=30)
    FName = models.CharField(max_length=20)
    LName = models.CharField(max_length=20)
    Address = models.CharField(max_length=50)
    OID = models.IntegerField()
    Description = models.CharField(max_length=100)
    QText = models.CharField(max_length=100)

class User(models.Model):
    Name = models.CharField(max_length=20)
    EMail = models.EmailField(max_length=30)
    RandomCode = models.CharField(max_length=20)
    AcivityCode = models.CharField(max_length=20)
    State = models.IntegerField(default=0)
