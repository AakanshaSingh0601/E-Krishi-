# Generated by Django 3.1.6 on 2021-03-25 06:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0003_auto_20210325_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crops',
            name='cimage',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='farmers',
            name='entrytime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 11, 46, 0, 812499)),
        ),
    ]
