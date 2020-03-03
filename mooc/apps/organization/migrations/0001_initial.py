# Generated by Django 2.0 on 2020-03-03 09:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='城市名称')),
                ('desc', models.CharField(max_length=255, verbose_name='描述信息')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '城市地址',
                'verbose_name_plural': '城市地址',
                'db_table': 'CityDict',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='机构名称')),
                ('desc', models.TextField(verbose_name='机构描述信息')),
                ('catgory', models.CharField(choices=[('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')], default='pxjg', max_length=50, verbose_name='机构类别')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('org_tag', models.CharField(default='全国知名', max_length=4, verbose_name='机构类型')),
                ('image', models.ImageField(blank=True, null=True, upload_to='org/%Y/%m', verbose_name='机构封面图')),
                ('address', models.CharField(max_length=100, verbose_name='机构地址')),
                ('kcs', models.IntegerField(default=0, verbose_name='课程数')),
                ('xxrs', models.IntegerField(default=0, verbose_name='学习人数')),
                ('lxfs', models.CharField(default='010-00000000', max_length=20, verbose_name='联系电话')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CityDict', verbose_name='所在城市')),
            ],
            options={
                'verbose_name': '课程机构',
                'verbose_name_plural': '课程机构',
                'db_table': 'CourseOrg',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='教师名称')),
                ('work_years', models.IntegerField(default=0, verbose_name='工作年限')),
                ('work_comfany', models.CharField(max_length=50, verbose_name='就职公司')),
                ('work_position', models.CharField(max_length=60, verbose_name='公司职业')),
                ('points', models.CharField(max_length=30, verbose_name='教学特点')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('teacher_arg', models.IntegerField(default=20, verbose_name='讲师年龄')),
                ('teacher_td', models.CharField(blank=True, max_length=50, null=True, verbose_name='教学特点')),
                ('image', models.ImageField(blank=True, null=True, upload_to='js/%Y/%m', verbose_name='教师图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='所属机构')),
            ],
            options={
                'verbose_name': '教师信息',
                'verbose_name_plural': '教师信息',
                'db_table': 'Teacher',
            },
        ),
    ]
