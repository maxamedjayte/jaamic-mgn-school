# Generated by Django 4.2.5 on 2023-09-28 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_students_living_students_mothername_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='dateOfBirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='registredDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
