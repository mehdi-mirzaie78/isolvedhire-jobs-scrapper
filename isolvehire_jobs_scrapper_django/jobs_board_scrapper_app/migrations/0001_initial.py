# Generated by Django 4.1.7 on 2023-03-09 20:22

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('url', models.URLField(unique=True, verbose_name='URL')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Location')),
                ('pay', models.CharField(blank=True, max_length=255, null=True, verbose_name='Pay')),
                ('pay_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Pay Type')),
                ('employment_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Employment Type')),
                ('job_benefits', models.CharField(blank=True, max_length=255, null=True, verbose_name='Job Benefits')),
                ('job_description', models.TextField(blank=True, null=True, verbose_name='Job Description')),
            ],
            options={
                'ordering': ('-modified', '-pay'),
            },
        ),
    ]
