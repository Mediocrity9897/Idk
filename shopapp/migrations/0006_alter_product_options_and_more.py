# Generated by Django 5.1.6 on 2025-03-18 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_order_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='descount',
            new_name='discount',
        ),
    ]
