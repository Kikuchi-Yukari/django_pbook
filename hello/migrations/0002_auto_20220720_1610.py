# Generated by Django 3.0.4 on 2022-07-20 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pbook',
            name='pbook_image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
