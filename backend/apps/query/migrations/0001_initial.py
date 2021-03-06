# Generated by Django 2.0.4 on 2020-04-17 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('db', '0002_auto_20200401_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuerySqlLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', null=True, verbose_name='更新时间')),
                ('comment', models.TextField(blank=True, help_text='备注', null=True, verbose_name='备注')),
                ('operator', models.CharField(blank=True, max_length=64, null=True, verbose_name='查询人')),
                ('dbname', models.CharField(blank=True, max_length=64, null=True, verbose_name='查询数据库')),
                ('sql', models.TextField(blank=True, verbose_name='查询sql')),
                ('mysqlinst', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='querysqllog_mysqlinst', to='db.MySQLInst', verbose_name='查询实例')),
            ],
            options={
                'verbose_name': 'sql查询日志表',
                'verbose_name_plural': 'sql查询日志表',
            },
        ),
    ]
