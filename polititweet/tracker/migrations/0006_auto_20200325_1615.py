# Generated by Django 2.2.5 on 2020-03-25 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20190408_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='full_text',
            field=models.TextField(blank=True, db_index=True, default=None, null=True),
        )
    ]
