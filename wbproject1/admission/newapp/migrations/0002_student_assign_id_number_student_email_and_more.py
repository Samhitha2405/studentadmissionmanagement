# Generated by Django 5.0.1 on 2024-02-21 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='assign_id_number',
            field=models.CharField(default='N/A', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='mother_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='parent_phone_number',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='student',
            name='student_phone_number',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='student',
            name='aadhar_number',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default='1900-01-01'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
