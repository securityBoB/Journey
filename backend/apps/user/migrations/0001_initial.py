# Generated by Django 2.0.4 on 2020-04-16 14:53

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mobile', models.CharField(blank=True, max_length=11, verbose_name='电话')),
                ('webcat', models.CharField(blank=True, max_length=128, verbose_name='微信')),
                ('comment', models.CharField(blank=True, max_length=64, verbose_name='备注')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('jwt_secret', models.UUIDField(default=uuid.UUID('ef9dc2b0-49ea-4bd6-bce8-ee243cdfb056'), verbose_name='用户jwt加密秘钥')),
            ],
            options={
                'verbose_name': '用户(Users)',
                'verbose_name_plural': '用户(Users)',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='菜单名称')),
                ('parent_id', models.IntegerField(blank=True, verbose_name='父菜单ID，一级菜单为0')),
                ('url', models.CharField(blank=True, max_length=255, verbose_name='菜单对应url')),
                ('mtype', models.IntegerField(blank=True, verbose_name='菜单类型 0:目录 1:菜单 2:内部跳转url ')),
                ('icon', models.CharField(blank=True, max_length=255, verbose_name='菜单对应图标')),
                ('creator', models.CharField(blank=True, max_length=64, verbose_name='创建人')),
                ('modifier', models.CharField(blank=True, max_length=64, verbose_name='最后修改人')),
                ('del_flag', models.IntegerField(blank=True, verbose_name='是否删除 -1:删除 0:正常')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('comment', models.CharField(blank=True, max_length=64, verbose_name='备注')),
            ],
            options={
                'verbose_name': '菜单表',
                'verbose_name_plural': '菜单表',
            },
        ),
        migrations.CreateModel(
            name='Perms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='后端api名称')),
                ('api', models.CharField(blank=True, max_length=255, verbose_name='后端api接口地址')),
                ('module_perms', models.CharField(blank=True, max_length=255, verbose_name='后端接口标识')),
                ('perms', models.CharField(blank=True, max_length=255, verbose_name='授权(多个用逗号分隔，如sys:user:post,sys:user:patch)')),
                ('creator', models.CharField(blank=True, max_length=64, verbose_name='创建人')),
                ('modifier', models.CharField(blank=True, max_length=64, verbose_name='最后修改人')),
                ('del_flag', models.IntegerField(blank=True, verbose_name='是否删除 -1:删除 0:正常')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('comment', models.CharField(blank=True, max_length=64, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, verbose_name='角色名称')),
                ('menu', models.ManyToManyField(blank=True, related_name='role_menu', to='user.Menu')),
                ('perms', models.ManyToManyField(blank=True, related_name='role_perms', to='user.Perms')),
            ],
            options={
                'verbose_name': '角色表',
                'verbose_name_plural': '角色表',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=64, unique=True)),
                ('comment', models.CharField(blank=True, max_length=128)),
            ],
            options={
                'verbose_name': '用户组',
                'verbose_name_plural': '用户组',
            },
        ),
        migrations.AddField(
            model_name='users',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_group', to='user.UserGroup'),
        ),
        migrations.AddField(
            model_name='users',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='users',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='user_role', to='user.Role', verbose_name='拥有的所有角色'),
        ),
        migrations.AddField(
            model_name='users',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
