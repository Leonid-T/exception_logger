# Generated by Django 5.0.4 on 2024-04-15 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CeleryExceptionDataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('args', models.JSONField(default=list, verbose_name='args')),
                ('kwargs', models.JSONField(default=dict, verbose_name='kwargs')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Throw data',
                'verbose_name_plural': 'Throw data',
            },
        ),
        migrations.CreateModel(
            name='CeleryExceptionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=512, verbose_name='Task')),
                ('exception', models.TextField()),
                ('traceback', models.TextField()),
                ('count', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('last_throw', models.DateTimeField(auto_now=True, verbose_name='Last throw')),
                ('first_throw', models.DateTimeField(auto_now_add=True, verbose_name='First throw')),
            ],
            options={
                'verbose_name': 'Celery Exception',
                'verbose_name_plural': 'Celery Exceptions',
            },
        ),
        migrations.CreateModel(
            name='ExceptionDataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_url', models.CharField(max_length=128)),
                ('data', models.JSONField(default=dict, verbose_name='Body')),
                ('query_params', models.JSONField(default=dict, verbose_name='Query params')),
                ('headers', models.JSONField(default=dict, verbose_name='Headers')),
                ('cookies', models.JSONField(default=dict, verbose_name='Cookies')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Throw data',
                'verbose_name_plural': 'Throw data',
            },
        ),
        migrations.CreateModel(
            name='ExceptionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('GET', 'Get'), ('POST', 'Post'), ('PUT', 'Put'), ('PATCH', 'Patch'), ('DELETE', 'Delete'), ('HEAD', 'Head'), ('OPTIONS', 'Options')], max_length=8, verbose_name='Request method')),
                ('path', models.CharField(max_length=512, verbose_name='Request path')),
                ('exception', models.CharField(max_length=256)),
                ('traceback', models.TextField()),
                ('count', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('last_throw', models.DateTimeField(auto_now=True, verbose_name='Last throw')),
                ('first_throw', models.DateTimeField(auto_now_add=True, verbose_name='Fast throw')),
            ],
            options={
                'verbose_name': 'Exception',
                'verbose_name_plural': 'Exceptions',
            },
        ),
        migrations.CreateModel(
            name='NoLogCeleryException',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exception', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'No log Celery Exception',
                'verbose_name_plural': 'No log Celery Exceptions',
            },
        ),
        migrations.CreateModel(
            name='NoLogException',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exception', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'No log Exception',
                'verbose_name_plural': 'No log Exceptions',
            },
        ),
        migrations.CreateModel(
            name='RequestTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('GET', 'Get'), ('POST', 'Post'), ('PUT', 'Put'), ('PATCH', 'Patch'), ('DELETE', 'Delete'), ('HEAD', 'Head'), ('OPTIONS', 'Options')], max_length=8, verbose_name='Request method')),
                ('path', models.CharField(max_length=512, verbose_name='Request path')),
                ('average_time', models.FloatField(default=0, verbose_name='Average request time')),
                ('dispersion', models.FloatField(default=0, verbose_name='Dispersion')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Quantity')),
            ],
            options={
                'verbose_name': 'Request time',
                'verbose_name_plural': 'Request times',
            },
        ),
        migrations.AddConstraint(
            model_name='celeryexceptionmodel',
            constraint=models.UniqueConstraint(fields=('task', 'exception'), name='exception_task'),
        ),
        migrations.AddField(
            model_name='celeryexceptiondatamodel',
            name='exception',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exception_logger.celeryexceptionmodel'),
        ),
        migrations.AddConstraint(
            model_name='exceptionmodel',
            constraint=models.UniqueConstraint(fields=('method', 'path', 'exception'), name='exception_path'),
        ),
        migrations.AddField(
            model_name='exceptiondatamodel',
            name='exception',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exception_logger.exceptionmodel'),
        ),
        migrations.AddConstraint(
            model_name='requesttime',
            constraint=models.UniqueConstraint(fields=('method', 'path'), name='request_path'),
        ),
    ]
