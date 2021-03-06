# Generated by Django 3.0.3 on 2020-05-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0002_auto_20200521_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairorder',
            name='begintime',
            field=models.DateField(auto_now_add=True, default=None, verbose_name='开始时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='repairorder',
            name='content',
            field=models.CharField(default=None, max_length=256, verbose_name='投诉内容'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='repairorder',
            name='overtime',
            field=models.DateField(default=None, verbose_name='结束时间'),
        ),
    ]
