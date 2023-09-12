from django.db import models

# Create your models here.


class  Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField(max)
    message=models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name

class News(models.Model):
    email=models.EmailField(max_length=100)


    def __str__(self) -> str:
        return self.email

class Dashboard(models.Model):
    website=models.URLField()
    date=models.DateTimeField()
    data=models.CharField(max_length=100)
    
class Messages(models.Model):
    writer=models.CharField(max_length=100)
    time=models.DateTimeField()
    mess=models.CharField(max_length=100)




class Fake(models.Model):
    title = models.CharField(max_length=100)
    company_element = models.CharField(max_length=100)
    location_element =models.CharField(max_length=100)


class NotePad(models.Model):
    note=models.CharField(max_length=150)
    

class Remote(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    time_posted=models.CharField(max_length=100)
    website=models.URLField()


class First(models.Model):
    info=models.CharField(max_length=100)
    website=models.URLField()

class Second(models.Model):
    info=models.CharField(max_length=100)
    website=models.URLField()

class Third(models.Model):
    info=models.CharField(max_length=100)
    website=models.URLField()

