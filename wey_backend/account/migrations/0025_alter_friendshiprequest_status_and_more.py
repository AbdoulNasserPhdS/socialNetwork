# Generated by Django 5.0.3 on 2024-04-18 04:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_alter_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendshiprequest',
            name='status',
            field=models.CharField(choices=[('sent', 'sent'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='sent', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 18, 0, 44, 24, 879722)),
        ),
    ]
