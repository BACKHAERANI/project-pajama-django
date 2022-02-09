# Generated by Django 3.2.12 on 2022-02-09 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('clothes_num', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('category', models.IntegerField(choices=[(0, 'TOP'), (1, 'BLOUSE & SHIRT'), (2, 'DRESS'), (3, 'PANTS'), (4, 'SKIRT'), (5, 'OUTER'), (6, 'ACC & CAP')])),
                ('price', models.IntegerField()),
                ('region', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('img1', models.ImageField(blank=True, upload_to='redanse/clothes/%Y/%m/%d/%H/%M/%S')),
                ('img2', models.ImageField(blank=True, upload_to='redanse/clothes/%Y/%m/%d/%H/%M/%S')),
                ('img3', models.ImageField(blank=True, upload_to='redanse/clothes/%Y/%m/%d/%H/%M/%S')),
                ('img4', models.ImageField(blank=True, upload_to='redanse/clothes/%Y/%m/%d/%H/%M/%S')),
                ('img5', models.ImageField(blank=True, upload_to='redanse/clothes/%Y/%m/%d/%H/%M/%S')),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-clothes_num'],
            },
        ),
    ]
