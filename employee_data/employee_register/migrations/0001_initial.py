# Generated by Django 5.2 on 2025-04-04 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empid', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('number', models.CharField(max_length=10)),
                ('role', models.CharField(choices=[('IT', 'IT'), ('Developer', 'Developer'), ('Admin', 'Admin'), ('Accounts', 'Accounts')], max_length=20)),
            ],
        ),
    ]
