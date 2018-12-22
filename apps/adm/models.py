#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Supplier(models.Model):
    """
    分销商管理
    """
    company = models.CharField(max_length=30, verbose_name="公司名称")
    address = models.CharField(max_length=100, verbose_name="地址")
    linkname = models.CharField(max_length=20, verbose_name="联系人")
    phone = models.CharField(max_length=20, verbose_name="联系电话")
    status = models.BooleanField(default=True, verbose_name="状态")
    belongs_to = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="责任人")
    desc = models.TextField(blank=True, null=True, verbose_name="备注")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "分销商管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.company


class Customer(models.Model):
    """
    客户信息
    """
    unit = models.CharField(max_length=50, verbose_name="客户单位")
    address = models.CharField(max_length=100, verbose_name="地址")
    name = models.CharField(max_length=20, verbose_name="联系人")
    phone = models.CharField(max_length=30, verbose_name="联系电话")
    belongs_to = models.ForeignKey(User, blank=True, null=True , on_delete=models.SET_NULL, verbose_name="责任人")
    status = models.BooleanField(default=True, verbose_name="状态")
    desc = models.TextField(blank=True, null=True, verbose_name="备注")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "客户管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.unit


class AssetType(models.Model):
    """
    资产类型
    """
    name = models.CharField(max_length=30, verbose_name="类型名称", help_text="类型名称")
    desc = models.TextField(blank=True, null=True, verbose_name="备注")
    parent = models.ForeignKey("self", null=True, blank=True, verbose_name="父类资产")
    level = models.CharField(max_length=20,verbose_name='等级',default="")
    status = models.CharField(max_length=30,verbose_name="状态",default="")


    class Meta:
        verbose_name = "资产类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Asset(models.Model):
    asset_status = (
        ("0", "闲置"),
        ("1", "在用"),
        ("2", "维修"),
        ("3", "报废"),
        ("4", "售出")
    )
    warehouse_choices = (
        ("0", "南京"),
        ("1", "苏州"),
    )
    assetNum = models.CharField(max_length=128, default="", verbose_name="资产编号")
    assetType = models.ForeignKey(AssetType, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="资产类型")
    brand = models.CharField(max_length=20, blank=True, null=True, verbose_name="品牌")
    model = models.CharField(max_length=30, default="", verbose_name="型号")
    warehouse = models.CharField(choices=warehouse_choices, default="1", max_length=20, verbose_name="仓库")
    price = models.IntegerField(blank=True, null=True, verbose_name="价格")
    buyDate = models.DateField(verbose_name="购买日期")
    warrantyDate = models.DateField(verbose_name="到保日期")
    status = models.CharField(choices=asset_status, max_length=20, default="1", verbose_name="资产状态")
    customer = models.CharField(max_length=80, default="", blank=True, null=True, verbose_name="客户信息")
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="使用人")
    operator = models.CharField(max_length=20, default="", verbose_name="入库人")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    desc = models.TextField(default="", blank=True, null=True, verbose_name="备注信息")

    class Meta:
        verbose_name = "资产管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.assetNum


class AssetFile(models.Model):
    asset = models.ForeignKey(Asset, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="资产")
    upload_user = models.CharField(max_length=20, verbose_name="上传人")
    file_content = models.ImageField(upload_to="asset_file/%Y/%m", null=True, blank=True, verbose_name="资产文件")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")


class AssetLog(models.Model):
    asset = models.ForeignKey(Asset, verbose_name="资产")
    operator = models.CharField(max_length=20, verbose_name="操作人")
    desc = models.TextField(default="", verbose_name="备注")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Mate:
        verbose_name = "变更记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.asset


class ServiceInfo(models.Model):
    content = models.TextField(verbose_name="记录内容")
    writer = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="记录人")
    is_reminding = models.BooleanField(default=False, verbose_name="邮件消息提醒")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Mate:
        verbose_name = "服务记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class EquipmentType(models.Model):
    """
    设备类型
    """
    name = models.CharField(max_length=30, verbose_name="类型名称", help_text="类型名称")
    desc = models.TextField(blank=True, null=True, verbose_name="备注")

    class Meta:
        verbose_name = "设备类型"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name


class Equipment(models.Model):
    number = models.CharField(max_length=30, default="", verbose_name="设备编号")
    equipment_type = models.ForeignKey(EquipmentType, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="设备类型")
    equipment_model = models.CharField(max_length=50, default="", verbose_name="设备型号")
    buy_date = models.DateField(verbose_name="购买日期")
    warranty_date = models.DateField(verbose_name="质保日期")
    accounting = models.BooleanField(default=False, verbose_name="费用核算状态")
    config_desc = models.TextField(blank=True, null=True, verbose_name="配置说明")
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="客户信息")
    supplier = models.ForeignKey(Supplier, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="分销商")
    service_info = models.ManyToManyField(ServiceInfo, blank=True, verbose_name="服务记录")

    class Meta:
        verbose_name = "设备管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.number



