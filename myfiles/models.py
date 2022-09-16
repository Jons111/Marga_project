from django.db import models

# Create your models here.
class Type(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi
class Project(models.Model):
    nomi = models.CharField(max_length=30)
    manzil = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='media')
    tur = models.ForeignKey(Type,on_delete=models.CASCADE)
    vaqt = models.DateTimeField(auto_now=True)

class Messagelar(models.Model):
    ism = models.CharField(max_length=30)
    fam = models.CharField(max_length=30)
    mail = models.EmailField(max_length=30)
    matn = models.TextField()
    vaqt = models.DateTimeField(auto_now=True)