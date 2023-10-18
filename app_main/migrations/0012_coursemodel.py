# Generated by Django 4.2.6 on 2023-10-18 17:26

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0011_delete_noticeimages_rename_post_title_notice_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=125, null=True, verbose_name='course name')),
                ('slug', models.SlugField(blank=True, editable=False, null=True)),
                ('code_name', models.CharField(max_length=125, null=True, verbose_name='course code name')),
                ('course_article', models.TextField(max_length=500, null=True, verbose_name='course article')),
                ('cover_image', models.ImageField(help_text='image size: w-800, h-500', null=True, upload_to='course-cover-images', verbose_name='course cover image')),
                ('course_glance', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('total_student_seat', models.CharField(max_length=125, null=True)),
                ('total_student', models.CharField(max_length=125, null=True)),
                ('total_graduated', models.CharField(max_length=125, null=True)),
                ('total_credit', models.CharField(blank=True, help_text="it's mandatory for hon's courses", max_length=125, null=True)),
                ('per_semester_fee', models.CharField(blank=True, help_text="it's mandatory for hon's courses", max_length=125, null=True)),
                ('total_tuition_fee', models.CharField(blank=True, help_text="it's mandatory for hon's courses", max_length=125, null=True)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
    ]
