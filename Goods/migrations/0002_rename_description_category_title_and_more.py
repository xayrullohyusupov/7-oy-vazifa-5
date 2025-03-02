# Generated by Django 5.1b1 on 2024-07-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='description',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='category',
            name='is_active',
        ),
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
