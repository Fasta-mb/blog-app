# Generated by Django 4.1.3 on 2022-12-11 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0004_alter_profile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
