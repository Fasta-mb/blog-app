# Generated by Django 4.1.3 on 2022-12-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='followed_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
