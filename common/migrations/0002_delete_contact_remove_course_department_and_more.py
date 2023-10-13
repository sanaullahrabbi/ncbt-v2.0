# Generated by Django 4.0.2 on 2022-02-08 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='course',
            name='department',
        ),
        migrations.RemoveField(
            model_name='enroll',
            name='course',
        ),
        migrations.RemoveField(
            model_name='enroll',
            name='student',
        ),
        migrations.RemoveField(
            model_name='financial',
            name='student',
        ),
        migrations.DeleteModel(
            name='Notice',
        ),
        migrations.RemoveField(
            model_name='result',
            name='course',
        ),
        migrations.RemoveField(
            model_name='result',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentregistrationcollage',
            name='user',
        ),
        migrations.RemoveField(
            model_name='studentregistrationuni',
            name='department',
        ),
        migrations.RemoveField(
            model_name='studentregistrationuni',
            name='user',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Enroll',
        ),
        migrations.DeleteModel(
            name='Financial',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
        migrations.DeleteModel(
            name='StudentRegistrationCollage',
        ),
        migrations.DeleteModel(
            name='StudentRegistrationUni',
        ),
    ]
