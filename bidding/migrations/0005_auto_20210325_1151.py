# Generated by Django 3.1.6 on 2021-03-25 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0004_auto_20210325_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crops',
            name='cimage',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='farmers',
            name='entrytime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 11, 51, 12, 263194)),
        ),
    ]