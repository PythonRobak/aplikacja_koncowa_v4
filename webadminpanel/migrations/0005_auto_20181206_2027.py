# Generated by Django 2.1.4 on 2018-12-06 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webadminpanel', '0004_auto_20181206_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
