# Generated by Django 4.2.1 on 2023-05-31 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_nutrient_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nutrient',
            options={'ordering': ('-date_created',)},
        ),
    ]
