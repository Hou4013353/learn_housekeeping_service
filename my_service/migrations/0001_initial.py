# Generated by Django 3.1.7 on 2021-04-06 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('user_id', models.AutoField(max_length=255, primary_key=True, serialize=False)),
                ('nick_name', models.CharField(max_length=255)),
                ('phone_num', models.IntegerField(max_length=32)),
                ('user_header', models.CharField(max_length=255)),
                ('wx_openid', models.CharField(max_length=255)),
                ('wx_session_key', models.CharField(max_length=255)),
                ('registration_time', models.DateTimeField()),
                ('registrant', models.CharField(max_length=255)),
                ('revision_time', models.DateTimeField()),
                ('reviser', models.CharField(max_length=255)),
            ],
        ),
    ]