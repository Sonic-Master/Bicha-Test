# Generated by Django 2.2.6 on 2020-04-18 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anshaj', '0010_interview_attended_datas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shortlisted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shortlisted_candidates_id', models.CharField(max_length=200)),
            ],
        ),
    ]
