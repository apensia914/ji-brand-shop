from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    """ Custom User Model """

    #Bank lists
    BANK_CHOICES = [
        ("--은행선택--", "--은행선택--"),
        ("신한은행", "신한은행"),
        ("우리은행", "우리은행"),
        ("하나은행", "하나은행"),
        ("IBK기업은행", "IBK기업은행"),
        ("KDB산업은행", "KDB산업은행"),
        ("대구은행", "대구은행"),
        ("부산은행", "부산은행"),
        ("경남은행", "경남은행"),
        ("광주은행", "광주은행"),
        ("전북은행", "전북은행"),
        ("제주은행", "제주은행"),
        ("카카오뱅크", "카카오뱅크"),
        ("기타", "기타"),
    ]
    
    main_address = models.CharField(max_length=100, verbose_name="Main address")
    sub_address = models.CharField(max_length=50, verbose_name="Sub address")
    zipcode = models.IntegerField(verbose_name="Zip code")
    phone_num = models.IntegerField(verbose_name="Phone number")
    mobile_num = models.IntegerField(verbose_name="Mobile phone number")
    # Bank Info
    bank_holder = models.CharField(max_length=10, verbose_name="Bank holder's name")
    bank = models.CharField(max_length=10, verbose_name="Bank name", choices=BANK_CHOICES, default="--은행선택--")
    bank_account_num = models.CharField(max_length=20, verbose_name="Bank account number")

    def __str__(self):
        return self.username
    
    class Meta: 
        verbose_name = "User"
        verbose_name_plural = "Users"