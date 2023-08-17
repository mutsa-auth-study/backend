# Generated by Django 3.2.20 on 2023-08-17 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('exam_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('qualgbcd', models.CharField(max_length=100)),
                ('qualgbnm', models.CharField(max_length=100)),
                ('seriescd', models.CharField(max_length=100)),
                ('seriesnm', models.CharField(max_length=100)),
                ('jmcd', models.CharField(max_length=100)),
                ('jmfldnm', models.CharField(max_length=100)),
                ('obligfldcd', models.CharField(blank=True, max_length=100)),
                ('obligfldnm', models.CharField(blank=True, max_length=100)),
                ('mdobligfldcd', models.CharField(blank=True, max_length=100)),
                ('mdobligfldnm', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ExamRecent',
            fields=[
                ('recent_id', models.AutoField(primary_key=True, serialize=False)),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.exam')),
            ],
        ),
        migrations.CreateModel(
            name='ExamPlan',
            fields=[
                ('exam_plan_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('implYy', models.CharField(max_length=100)),
                ('implSeq', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('docRegStartDt', models.CharField(blank=True, max_length=100)),
                ('docRegEndDt', models.CharField(blank=True, max_length=100)),
                ('docExamStartDt', models.CharField(blank=True, max_length=100)),
                ('docExamEndDt', models.CharField(blank=True, max_length=100)),
                ('docPassDt', models.CharField(blank=True, max_length=100)),
                ('pracRegStartDt', models.CharField(blank=True, max_length=100)),
                ('pracRegEndDt', models.CharField(blank=True, max_length=100)),
                ('pracExamStartDt', models.CharField(blank=True, max_length=100)),
                ('pracExamEndDt', models.CharField(blank=True, max_length=100)),
                ('pracPassDt', models.CharField(blank=True, max_length=100)),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.exam')),
            ],
        ),
        migrations.CreateModel(
            name='ExamFavorite',
            fields=[
                ('favorite_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.exam')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
