# Generated by Django 3.2.4 on 2021-08-12 12:36

import diploma.models
from django.db import migrations, models
import django.db.models.deletion
import lib.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_auto_20210812_1536'),
        ('course', '0051_auto_20210812_1536'),
        ('exercise', '0039_auto_20210812_1536'),
        ('diploma', '0003_alter_coursediplomadesign_availability'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursediplomadesign',
            options={'verbose_name': 'MODEL_NAME_COURSE_DIPLOMA_DESIGN', 'verbose_name_plural': 'MODEL_NAME_COURSE_DIPLOMA_DESIGN_PLURAL'},
        ),
        migrations.AlterModelOptions(
            name='studentdiploma',
            options={'verbose_name': 'MODEL_NAME_STUDENT_DIPLOMA', 'verbose_name_plural': 'MODEL_NAME_STUDENT_DIPLOMA_PLURAL'},
        ),
        migrations.AlterField(
            model_name='coursediplomadesign',
            name='availability',
            field=models.IntegerField(choices=[(1, 'INTERNAL_USERS'), (2, 'EXTERNAL_USERS'), (3, 'ALL_USERS')], default=2, verbose_name='LABEL_AVAILABILTY'),
        ),
        migrations.AlterField(
            model_name='coursediplomadesign',
            name='body',
            field=models.TextField(blank=True, verbose_name='LABEL_BODY'),
        ),
        migrations.AlterField(
            model_name='coursediplomadesign',
            name='course',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.courseinstance', verbose_name='LABEL_COURSE'),
        ),
        migrations.AlterField(
            model_name='coursediplomadesign',
            name='date',
            field=models.CharField(max_length=256, verbose_name='LABEL_DATE'),
        ),
        migrations.AlterField(
            model_name='coursediplomadesign',
            name='exercises_to_pass',
            field=models.ManyToManyField(blank=True, to='exercise.BaseExercise', verbose_name='LABEL_EXERCISES_TO_PASS'),
        ),
        migrations.AlterField(
            model_name='coursediplomadesign',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=diploma.models.build_upload_dir, verbose_name='LABEL_LOGO'),
        ),
        migrations.AlterField(
            model_name='coursediplomadesign',
            name='modules_to_pass',
            field=models.ManyToManyField(blank=True, to='course.CourseModule', verbose_name='LABEL_MODULES_TO_PASS'),
        ),
        migrations.AlterField(
            model_name='coursediplomadesign',
            name='pad_points',
            field=models.BooleanField(default=False, help_text='DIPLOMA_PAD_POINTS_HELPTEXT', verbose_name='LABEL_PAD_POINTS'),
        ),
        migrations.AlterField(
            model_name='coursediplomadesign',
            name='point_limits',
            field=lib.fields.JSONField(blank=True, help_text='DIPLOMA_POINT_LIMITS_HELPTEXT', verbose_name='LABEL_POINT_LIMITS'),
        ),
        migrations.AlterField(
            model_name='coursediplomadesign',
            name='signature_name',
            field=models.CharField(blank=True, max_length=256, verbose_name='LABEL_SIGNATURE_NAME'),
        ),
        migrations.AlterField(
            model_name='coursediplomadesign',
            name='signature_title',
            field=models.CharField(blank=True, max_length=256, verbose_name='LABEL_SIGNATURE_TITLE'),
        ),
        migrations.AlterField(
            model_name='coursediplomadesign',
            name='small_print',
            field=models.TextField(blank=True, verbose_name='LABEL_SMALL_PRINT'),
        ),
        migrations.AlterField(
            model_name='coursediplomadesign',
            name='title',
            field=models.TextField(blank=True, verbose_name='LABEL_TITLE'),
        ),
        migrations.AlterField(
            model_name='studentdiploma',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='LABEL_CREATED'),
        ),
        migrations.AlterField(
            model_name='studentdiploma',
            name='design',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diploma.coursediplomadesign', verbose_name='LABEL_DESIGN'),
        ),
        migrations.AlterField(
            model_name='studentdiploma',
            name='grade',
            field=models.PositiveIntegerField(default=0, verbose_name='LABEL_GRADE'),
        ),
        migrations.AlterField(
            model_name='studentdiploma',
            name='hashkey',
            field=models.CharField(max_length=32, unique=True, verbose_name='LABEL_HASHKEY'),
        ),
        migrations.AlterField(
            model_name='studentdiploma',
            name='name',
            field=models.CharField(max_length=255, verbose_name='LABEL_NAME'),
        ),
        migrations.AlterField(
            model_name='studentdiploma',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.userprofile', verbose_name='LABEL_PROFILE'),
        ),
    ]