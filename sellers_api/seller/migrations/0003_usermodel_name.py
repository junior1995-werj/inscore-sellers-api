# Generated by Django 4.0.4 on 2024-02-23 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_userauthmodel_sellermodel_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
