# Generated by Django 3.2.8 on 2022-03-15 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='no_image.png', upload_to=''),
        ),
    ]