# Generated by Django 5.1.3 on 2025-01-14 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_rename_name_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(null=True),
        ),
    ]