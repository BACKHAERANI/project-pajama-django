# Generated by Django 3.2.12 on 2022-02-09 10:19

import django.core.validators
from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('user_id', models.CharField(max_length=18, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(6), django.core.validators.RegexValidator(regex='^[a-zA-Z0-9]*$')])),
                ('username', models.CharField(max_length=20)),
                ('user_nickname', models.CharField(max_length=18, unique=True)),
                ('user_tel', models.CharField(help_text='입력예) 010-1234-1234', max_length=13, validators=[django.core.validators.RegexValidator('^\\d{3}-\\d{3,4}-\\d{4}$', message='오류')])),
                ('user_birth', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{4}-\\d{2}-\\d{2}$')])),
                ('user_genre', models.CharField(blank=True, choices=[('팝핀', '팝핀'), ('브레이킹', '브레이킹'), ('락킹', '락킹'), ('왁킹', '왁킹'), ('힙합', '힙합'), ('하우스', '하우스'), ('크럼프', '크럼프'), ('기타', '기타')], max_length=18)),
                ('user_type', models.IntegerField(choices=[(0, 0), (1, 1)], default=0)),
                ('user_auth', models.IntegerField(choices=[(0, 0), (1, 1)], default=0)),
                ('user_signupdate', models.DateTimeField(auto_now_add=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', user.models.CustomUserManager()),
            ],
        ),
    ]
