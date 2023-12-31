# Generated by Django 4.1 on 2022-10-03 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fmain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='NotePad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='fake',
            name='location_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.fmain'),
        ),
    ]
