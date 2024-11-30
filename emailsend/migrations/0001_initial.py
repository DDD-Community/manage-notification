# Generated by Django 5.1.2 on 2024-11-30 06:01

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='이메일 KEY ID')),
                ('title', models.CharField(max_length=200, verbose_name='이메일 제목')),
                ('body', tinymce.models.HTMLField(verbose_name='이메일 본문')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
            ],
            options={
                'verbose_name': '이메일 템플릿',
                'verbose_name_plural': '이메일 템플릿',
                'ordering': ['-updated_at'],
            },
        ),
    ]
