# Generated by Django 3.2.9 on 2022-02-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_community_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='community_num',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
