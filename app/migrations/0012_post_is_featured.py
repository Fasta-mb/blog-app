# Generated by Django 4.1.3 on 2023-01-13 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_post_num_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_featured',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
