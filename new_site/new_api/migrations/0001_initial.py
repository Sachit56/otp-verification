# Generated by Django 5.0 on 2023-12-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
