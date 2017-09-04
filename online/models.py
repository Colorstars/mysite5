from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)     # 字段，默认会多个id字段
    age = models.IntegerField()


# 用户个人信息
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(help_text='用户姓名', max_length=40, default='0')
    tel = models.CharField(help_text='电话号码', max_length=40)
    adds = models.CharField(help_text='地址', max_length=40)
    city = models.CharField(help_text='城市', max_length=40)
    postCode = models.IntegerField()

    def __unicode__(self):
        return self.user
