# Generated by Django 3.0.3 on 2020-05-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0004_auto_20200527_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='image',
            field=models.CharField(default='img/house/', max_length=64, verbose_name='图片路径'),
        ),
    ]