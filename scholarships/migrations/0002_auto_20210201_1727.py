# Generated by Django 3.1.5 on 2021-02-01 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='s_about',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='s_eligibility',
            field=models.CharField(max_length=200),
        ),
    ]
