from django.db import models
from my_service import models as user


# Create your models here.
# 课程表
class course_info(models.Model):

    course_id = models.ForeignKey("my_service.user_info", on_delete=models.DO_NOTHING)
    course_name = models.CharField(max_length=255)
    course_type = models.CharField(max_length=32)
    course_cover = models.CharField(max_length=255)
    tuition = models.DecimalField(max_digits=3, decimal_places=3)
    course_chapter = models.CharField(max_length=255)
    single_course = models.CharField(max_length=255)
    course_foundation = models.CharField(max_length=32)
    course_video = models.CharField(max_length=255)
    course_author = models.CharField(max_length=64)
    course_label = models.CharField(max_length=128)
    play_num = models.IntegerField()
    pay_num = models.IntegerField()
    registration_time = models.DateTimeField()
    registrant = models.CharField(max_length=255)
    revision_time = models.DateTimeField()
    reviser = models.CharField(max_length=255)


# 搜索栏中的热门推荐表
class search_recommend(models.Model):
    recommend_id = models.AutoField(primary_key=True)
    recommend_course = models.CharField(max_length=255)
    registration_time = models.DateTimeField()
    registrant = models.CharField(max_length=255)
    revision_time = models.DateTimeField()
    reviser = models.CharField(max_length=255)


# 主页的轮播图表
class publicity_pic(models.Model):
    Publicity_id = models.AutoField(primary_key=True)
    Publicity_pic = models.CharField(max_length=255)
    jump_url = models.CharField(max_length=255)
    registration_time = models.DateTimeField()
    registrant = models.CharField(max_length=255)
    revision_time = models.DateTimeField()
    reviser = models.CharField(max_length=255)


# 用户课程关联表
class user_course(models.Model):
    course_id = models.ForeignKey("course_info", on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey("my_service.user_info", on_delete=models.DO_NOTHING)
    registration_time = models.DateTimeField()
    registrant = models.CharField(max_length=255)
    revision_time = models.DateTimeField()
    reviser = models.CharField(max_length=255)