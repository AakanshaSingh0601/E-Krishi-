# Generated by Django 3.1.6 on 2021-03-25 05:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0002_auto_20210324_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='crops',
            name='cimage',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='farmers',
            name='entrytime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 11, 7, 1, 340697)),
        ),
    ]
