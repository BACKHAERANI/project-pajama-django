# Generated by Django 3.2.12 on 2022-02-07 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('clothes', '0002_alter_clothes_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_num', models.AutoField(primary_key=True, serialize=False)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('total_amount', models.IntegerField()),
                ('payment_method', models.CharField(choices=[('카드', '카드'), ('현금', '만나서 현금결제')], max_length=18)),
                ('total_price', models.IntegerField()),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'ordering': ['-payment_num'],
            },
        ),
        migrations.CreateModel(
            name='Payment_detail',
            fields=[
                ('payment_detail_num', models.AutoField(primary_key=True, serialize=False)),
                ('clothes_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.clothes')),
                ('payment_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.payment')),
            ],
            options={
                'ordering': ['-payment_detail_num'],
            },
        ),
    ]