# Generated by Django 4.1 on 2022-10-03 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_fake_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fake',
            name='website',
        ),
    ]
