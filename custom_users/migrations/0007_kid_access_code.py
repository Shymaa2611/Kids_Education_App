# Generated by Django 4.1.10 on 2023-09-18 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0006_kid'),
    ]

    operations = [
        migrations.AddField(
            model_name='kid',
            name='access_code',
            field=models.IntegerField(default=0),
        ),
    ]
