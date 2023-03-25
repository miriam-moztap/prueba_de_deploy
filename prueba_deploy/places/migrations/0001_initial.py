# Generated by Django 4.1.7 on 2023-03-24 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'places',
            },
        ),
    ]
