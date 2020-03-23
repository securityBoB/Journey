# Generated by Django 2.0.4 on 2020-03-09 17:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20200309_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perms',
            name='perms',
            field=models.CharField(blank=True, max_length=255, unique=True, verbose_name='授权(多个用逗号分隔，如sys:user:post,sys:user:patch)'),
        ),
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('eab54d28-d6e8-41d4-9662-6c95e78cc760'), verbose_name='用户jwt加密秘钥'),
        ),
    ]
