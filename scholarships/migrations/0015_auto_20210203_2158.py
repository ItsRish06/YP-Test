# Generated by Django 3.1.5 on 2021-02-03 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0014_auto_20210203_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='site_url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
