# Generated by Django 4.1.3 on 2022-12-02 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0002_alter_profile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
