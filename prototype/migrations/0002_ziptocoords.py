# Generated by Django 3.2.16 on 2022-11-10 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='zipToCoords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip', models.CharField(max_length=7)),
                ('name', models.CharField(max_length=200)),
                ('lat', models.CharField(max_length=200)),
                ('lon', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
    ]
