# Generated by Django 5.1b1 on 2024-07-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0002_rename_description_category_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productenter',
            name='old_quantity',
            field=models.IntegerField(blank=True),
        ),
    ]
