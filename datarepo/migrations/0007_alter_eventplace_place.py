# Generated by Django 3.2.3 on 2021-05-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datarepo', '0006_auto_20210528_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventplace',
            name='place',
            field=models.CharField(max_length=255),
        ),
    ]
