# Generated by Django 4.2.7 on 2024-01-08 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userpasswordreset_delete_resetpass'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserPasswordReset',
        ),
    ]