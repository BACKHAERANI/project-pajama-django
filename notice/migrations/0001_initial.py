# Generated by Django 3.2.12 on 2022-02-10 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('notice_num', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('img1', models.ImageField(blank=True, upload_to='redanse/notice/%Y/%m/%d/%H/%M/%S')),
                ('img2', models.ImageField(blank=True, upload_to='redanse/notice/%Y/%m/%d/%H/%M/%S')),
                ('img3', models.ImageField(blank=True, upload_to='redanse/notice/%Y/%m/%d/%H/%M/%S')),
                ('img4', models.ImageField(blank=True, upload_to='redanse/notice/%Y/%m/%d/%H/%M/%S')),
                ('img5', models.ImageField(blank=True, upload_to='redanse/notice/%Y/%m/%d/%H/%M/%S')),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-notice_num'],
            },
        ),
    ]
