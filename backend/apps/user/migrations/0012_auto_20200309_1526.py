# Generated by Django 2.0.4 on 2020-03-09 15:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20200309_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='perms',
            name='module_perms',
            field=models.CharField(blank=True, max_length=255, verbose_name='后端接口标识'),
        ),
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('31c6799b-5d4e-4345-bd77-2b6673dc44b9'), verbose_name='用户jwt加密秘钥'),
        ),
    ]
