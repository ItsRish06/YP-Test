# Generated by Django 3.1.5 on 2021-02-02 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0010_scholarship_site_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='date_test',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
