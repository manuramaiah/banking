# Generated by Django 5.0.1 on 2024-02-04 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0004_accounttype_applicationform_material_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationform',
            name='account_type',
        ),
        migrations.RemoveField(
            model_name='applicationform',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='applicationform',
            name='district',
        ),
        migrations.RemoveField(
            model_name='applicationform',
            name='materials_provided',
        ),
    ]
