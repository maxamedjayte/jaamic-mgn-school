# Generated by Django 4.2.5 on 2023-11-30 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_examentring_classe_examentring_classe'),
    ]

    operations = [
        migrations.AddField(
            model_name='exammarks',
            name='classe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.classe'),
        ),
    ]
