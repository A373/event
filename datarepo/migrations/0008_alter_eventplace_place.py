# Generated by Django 3.2.3 on 2021-05-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datarepo', '0007_alter_eventplace_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventplace',
            name='place',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
