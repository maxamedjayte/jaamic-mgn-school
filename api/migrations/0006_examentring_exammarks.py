# Generated by Django 4.2.5 on 2023-11-28 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_students_dateofbirth_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamEntring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examName', models.CharField(max_length=255)),
                ('examDate', models.DateField(blank=True, null=True)),
                ('academicYear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.academicyear')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classe')),
            ],
        ),
        migrations.CreateModel(
            name='ExamMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(blank=True, null=True)),
                ('dateModified', models.DateTimeField(auto_now=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.examentring')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.students')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subject')),
            ],
        ),
    ]
