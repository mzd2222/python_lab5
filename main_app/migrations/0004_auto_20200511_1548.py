# Generated by Django 3.0.5 on 2020-05-11 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200511_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionaries',
            name='chinese',
            field=models.CharField(max_length=500),
        ),
    ]
