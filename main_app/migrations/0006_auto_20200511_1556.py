# Generated by Django 3.0.5 on 2020-05-11 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20200511_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionaries',
            name='chinese',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='dictionaries',
            name='eggs',
            field=models.TextField(),
        ),
    ]
