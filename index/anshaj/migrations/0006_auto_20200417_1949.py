# Generated by Django 2.2.6 on 2020-04-17 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anshaj', '0005_job_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job_category',
            old_name='categorys',
            new_name='job_cat',
        ),
    ]
