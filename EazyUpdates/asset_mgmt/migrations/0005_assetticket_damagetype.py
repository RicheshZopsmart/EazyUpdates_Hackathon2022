# Generated by Django 4.1.2 on 2022-10-08 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_mgmt', '0004_alter_assetticket_asset'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetticket',
            name='damagetype',
            field=models.CharField(max_length=10, null=True),
        ),
    ]