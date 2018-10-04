# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

Choices = (

        ('Bill Payment', 'Bill Payment'),
        ('Sent to the Friend', 'Sent to the Friend'),
        ('Received from the Friend', 'Received from the Friend'),
        ('Airtime Purchase', 'Airtime Purchase'),
        ('Airtime Cashing', 'Airtime Cashing'),
        
        )

Choices1 = (

        ('Success', 'Success'),
        ('Failed', 'Failed'),
        
        )

Choices2 = (

        ('Wallet', 'Wallet'),
        ('Bank', 'Bank'),
        
        )

Choices3 = (

        ('Cr', 'CR'),
        ('Dr', 'DR'),
        
        )
Choicess = (

        ('Good', 'Good'),
        ('Average', 'Average'),
        ('Excellent', 'Excellent'),
        ('Bad', 'Bad'),
        )
Choices8 = (

        ('TV, Internet e Telecomunicações', 'TV, Internet e Telecomunicações'),
        ('Servicos Publicos', 'Servicos Publicos'),
        ('Impostos e Taxas', 'Impostos e Taxas'),
        ('Companhias Aereas', 'Companhias Aereas'),
        ('Empresas De Seguros', 'Empresas De Seguros'),
        ('Universidades e Ensino Académico Superior', 'Universidades e Ensino Académico Superior'),
        )
    


class User(models.Model):
    id = models.BigIntegerField(primary_key = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    middle_name = models.CharField(max_length = 100)
    addr1 = models.CharField(max_length = 100)
    addr2 = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    Country = models.CharField(max_length = 100)
    zip1 = models.CharField(max_length = 100)
    Email = models.CharField(max_length = 100)
    Mobile = models.CharField(max_length = 100)
    Review = models.CharField(max_length = 100)
    SignUp_Date = models.DateField(auto_now_add = True)
    wallet_balance = models.IntegerField(default = 0)
    Pro_pic = models.ImageField(upload_to = 'product')
    status = models.BooleanField(default = False)
    Feedback = models.CharField(max_length = 100,default = 'Good', choices = Choicess)
    FeedDate = models.DateField(default = '2018-01-01')
    def __str__(self):
        return str(self.id)

class Form(models.Model):
    start = models.DateField()
    end = models.DateField()

class Coupons(models.Model):
    Code = models.CharField(max_length = 100)
    ExpirationDate = models.DateField()
    CashBack = models.IntegerField()
    def __str__(self):
        return self.Code

class Services(models.Model):
    Service_type = models.CharField(max_length = 100, choices = Choices8)
    Provider_name = models.CharField(max_length = 150)
    complaint = models.CharField(max_length = 150, null = True)
    def __unicode__(self):
        return self.Service_type + " - " + self.Provider_name 




class Transaction(models.Model):
    transaction_id  = models.BigIntegerField(primary_key = True)
    transaction_type = models.CharField(max_length = 100, choices = Choices3)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    Date = models.DateField(auto_now_add = True)
    Amount = models.IntegerField()
    Payment_mode = models.CharField(max_length = 100, choices = Choices2)
    Description = models.CharField(max_length = 100, choices = Choices)
    Status = models.CharField(max_length = 100, choices = Choices1)

    def __str__(self):
        return str(self.user_id)
