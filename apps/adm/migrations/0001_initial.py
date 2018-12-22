# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-21 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetNum', models.CharField(default='', max_length=128, verbose_name='资产编号')),
                ('brand', models.CharField(blank=True, max_length=20, null=True, verbose_name='品牌')),
                ('model', models.CharField(default='', max_length=30, verbose_name='型号')),
                ('warehouse', models.CharField(choices=[('0', '南京'), ('1', '苏州')], default='1', max_length=20, verbose_name='仓库')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='价格')),
                ('buyDate', models.DateField(verbose_name='购买日期')),
                ('warrantyDate', models.DateField(verbose_name='到保日期')),
                ('status', models.CharField(choices=[('0', '闲置'), ('1', '在用'), ('2', '维修'), ('3', '报废'), ('4', '售出')], default='1', max_length=20, verbose_name='资产状态')),
                ('customer', models.CharField(blank=True, default='', max_length=80, null=True, verbose_name='客户信息')),
                ('operator', models.CharField(default='', max_length=20, verbose_name='入库人')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('desc', models.TextField(blank=True, default='', null=True, verbose_name='备注信息')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '资产管理',
            },
        ),
        migrations.CreateModel(
            name='AssetFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_user', models.CharField(max_length=20, verbose_name='上传人')),
                ('file_content', models.ImageField(blank=True, null=True, upload_to='asset_file/%Y/%m', verbose_name='资产文件')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
            ],
        ),
        migrations.CreateModel(
            name='AssetLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(max_length=20, verbose_name='操作人')),
                ('desc', models.TextField(default='', verbose_name='备注')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='AssetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='类型名称', max_length=30, verbose_name='类型名称')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '资产类型',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=50, verbose_name='客户单位')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('name', models.CharField(max_length=20, verbose_name='联系人')),
                ('phone', models.CharField(max_length=30, verbose_name='联系电话')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '客户管理',
                'verbose_name_plural': '客户管理',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='', max_length=30, verbose_name='设备编号')),
                ('equipment_model', models.CharField(default='', max_length=50, verbose_name='设备型号')),
                ('buy_date', models.DateField(verbose_name='购买日期')),
                ('warranty_date', models.DateField(verbose_name='质保日期')),
                ('accounting', models.BooleanField(default=False, verbose_name='费用核算状态')),
                ('config_desc', models.TextField(blank=True, null=True, verbose_name='配置说明')),
            ],
            options={
                'verbose_name': '设备管理',
                'verbose_name_plural': '设备管理',
            },
        ),
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='类型名称', max_length=30, verbose_name='类型名称')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '设备类型',
                'verbose_name_plural': '设备类型',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ServiceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='记录内容')),
                ('is_reminding', models.BooleanField(default=False, verbose_name='邮件消息提醒')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=30, verbose_name='公司名称')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('linkname', models.CharField(max_length=20, verbose_name='联系人')),
                ('phone', models.CharField(max_length=20, verbose_name='联系电话')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '分销商管理',
                'verbose_name_plural': '分销商管理',
            },
        ),
    ]
