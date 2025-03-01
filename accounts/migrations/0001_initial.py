# Generated by Django 5.0.4 on 2024-04-05 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_holder', models.CharField(max_length=50)),
                ('account_number', models.CharField(max_length=14, unique=True)),
                ('open_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
