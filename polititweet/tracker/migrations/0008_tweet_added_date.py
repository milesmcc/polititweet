# Generated by Django 2.1.7 on 2019-03-10 17:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_auto_20190310_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
