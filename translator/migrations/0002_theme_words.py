# Generated by Django 2.2.4 on 2020-03-27 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='words',
            field=models.ManyToManyField(to='translator.Word'),
        ),
    ]
