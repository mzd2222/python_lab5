# Generated by Django 3.0.5 on 2020-05-11 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200511_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionaries',
            name='chinese',
            field=models.CharField(default='#', max_length=200),
        ),
        migrations.AlterField(
            model_name='dictionaries',
            name='eggs',
            field=models.TextField(default='#'),
        ),
        migrations.AlterField(
            model_name='dictionaries',
            name='spell',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dictionaries',
            name='tp',
            field=models.CharField(default='#', max_length=200),
        ),
    ]