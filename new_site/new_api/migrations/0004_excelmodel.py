# Generated by Django 5.0 on 2023-12-29 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_api', '0003_category_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel', models.FileField(upload_to='excel')),
            ],
        ),
    ]