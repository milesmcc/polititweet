# Generated by Django 2.1.7 on 2019-03-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]