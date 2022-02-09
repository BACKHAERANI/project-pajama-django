# Generated by Django 3.2.12 on 2022-02-09 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
