from django.db import models


# Create your models here.

class user_info(models.Model):
    user_id = models.AutoField(primary_key=True)
    nick_name = models.CharField(max_length=255)
    phone_num = models.IntegerField()
    user_header = models.CharField(max_length=255)
    wx_openid = models.CharField(max_length=255)
    wx_session_key = models.CharField(max_length=255)
    password = models.CharField(null=True, max_length=255)
    registration_time = models.DateTimeField()
    registrant = models.CharField(max_length=255)
    revision_time = models.DateTimeField()
    reviser = models.CharField(max_length=255)

