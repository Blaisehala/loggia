# Generated by Django 4.0.4 on 2022-05-29 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_att',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='category',
            new_name='image_category',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='location',
            new_name='image_location',
        ),
    ]