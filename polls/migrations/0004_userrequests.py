# Generated by Django 2.1.4 on 2018-12-22 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20181222_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userrequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fanuname', models.CharField(max_length=100)),
                ('celuname', models.CharField(max_length=100)),
                ('fcontent', models.CharField(max_length=300)),
            ],
        ),
    ]