# Generated by Django 2.2 on 2020-12-26 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0004_auto_20201225_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_content',
            field=models.TextField(max_length=255),
        ),
    ]
