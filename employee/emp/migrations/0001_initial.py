# Generated by Django 5.2 on 2025-04-04 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('birth_date', models.DateField()),
                ('role', models.CharField(choices=[('accounts', 'Accounts'), ('it', 'IT'), ('dev', 'Development'), ('admin', 'Admin')], max_length=20)),
            ],
        ),
    ]
