# Generated by Django 3.0.5 on 2020-05-11 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dictionaries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spell', models.CharField(max_length=10)),
                ('tp', models.CharField(max_length=5)),
                ('chinese', models.CharField(max_length=20)),
                ('eggs', models.CharField(max_length=100)),
            ],
        ),
    ]