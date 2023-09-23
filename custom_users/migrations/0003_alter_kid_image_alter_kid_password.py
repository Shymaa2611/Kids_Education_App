# Generated by Django 4.1.10 on 2023-09-23 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0002_kid_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/images/'),
        ),
        migrations.AlterField(
            model_name='kid',
            name='password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]