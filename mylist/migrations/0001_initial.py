# Generated by Django 5.0.7 on 2024-07-11 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('name', models.CharField(max_length=200)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
