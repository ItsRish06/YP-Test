# Generated by Django 3.1.5 on 2021-02-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0017_auto_20210203_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='content',
            field=models.TextField(max_length=50000),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='slug',
            field=models.SlugField(blank=True, max_length=150),
        ),
    ]
