# Generated by Django 4.0.2 on 2022-03-17 13:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_comment_create_date_alter_post_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 17, 13, 44, 59, 697329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 17, 13, 44, 59, 696329, tzinfo=utc)),
        ),
    ]
