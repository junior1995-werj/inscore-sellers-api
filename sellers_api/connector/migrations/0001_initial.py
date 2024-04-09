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
            name='ConnectorsModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'connector_connectors',
            },
        ),
        migrations.CreateModel(
            name='SellerConnectorModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('connect_information', models.JSONField()),
                ('connector_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connector.connectorsmodel')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.sellermodel')),
            ],
            options={
                'db_table': 'sellers_connectors',
            },
        ),
    ]