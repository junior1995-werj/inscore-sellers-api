# Generated by Django 4.0.4 on 2024-02-22 13:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerGroupsModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('group_id', models.CharField(max_length=255)),
                ('group_name', models.CharField(max_length=255)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.sellermodel')),
            ],
            options={
                'db_table': 'sellers_groups',
            },
        ),
        migrations.CreateModel(
            name='SellerContactsModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.sellermodel')),
            ],
            options={
                'db_table': 'sellers_contacts',
            },
        ),
    ]
