from django.db import models

# Create your models here.


class Event(models.Model):
    id = models.IntegerField('id', primary_key=True, null=False, unique=True, auto_created=True)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.description

class User(models.Model):
    id = models.IntegerField('id', primary_key=True, null=False, unique=True, auto_created=True)
    first_name = models.CharField('First Name',max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    age=models.IntegerField('Age', default=0)
    birthday = models.DateField('Birthday')
    user_type = models.CharField('User Type', max_length=50)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.user_type}'
