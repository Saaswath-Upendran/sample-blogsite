# Generated by Django 4.0.2 on 2022-03-17 15:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_comment_create_date_alter_post_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=datetime.datetime(2022, 3, 17, 20, 43, 10, 66666), on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 17, 15, 10, 50, 859359, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 17, 15, 10, 50, 859359, tzinfo=utc)),
        ),
    ]