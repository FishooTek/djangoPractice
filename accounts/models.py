from django.db import models

# Create your models here.
class Accounts(models.Model):
    account_holder = models.CharField(max_length =50)
    account_number = models.CharField(unique=True,max_length = 14)
    open_date= models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.account_holder