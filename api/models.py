from django.db import models

# Create your models here.
# Creating Comapny Models

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=50,choices=
                                                (('IT','IT'),
                                                 ('NON IT','NON IT'),
                                                 ('Mobile Phone','Mobile Phone')
                                                 ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name 
# Creating Employee Models

class Employee(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=20)
    Address=models.CharField(max_length=200)
    Phone=models.CharField(max_length=10)
    About=models.TextField()
    Position=models.CharField(max_length=50,choices=( 
        ('manager','manager'),
        ('software developer','sd'),
        ('project lead','pl')
    ))

    company=models.ForeignKey(Company, on_delete=models.CASCADE)