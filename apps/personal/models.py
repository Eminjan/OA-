#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M

from django.db import models

from django.contrib.auth import get_user_model

from adm.models import Customer

User = get_user_model()


class WorkOrder(models.Model):
    type_choices = (('0', '初次安装'), ('1', '售后现场'), ('2', '远程支持'), ('3', '售前支持'))
    status_choices = (('0', '工单已退回'), ('1', '新建-保存'), ('2', '提交-等待审批'), ('3', '已审批-等待执行'), ('4', '已执行-等待确认'), ('5', '工单已完成'))
    number = models.CharField(max_length=10, verbose_name='工单号')
    title = models.CharField(max_length=50, verbose_name='标题')
    type = models.CharField(max_length=10, choices=type_choices, default='0', verbose_name='工单类型')
    status = models.CharField(max_length=10, choices=status_choices, default='0', verbose_name='工单状态')
    do_time = models.DateTimeField(default='', verbose_name='安排时间')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    content = models.CharField(max_length=300, verbose_name='工单内容')
    file_content = models.FileField(upload_to='file/%Y/%m', blank=True, null=True, verbose_name='项目资料')
    customer = models.ForeignKey(Customer, verbose_name='客户信息')
    proposer = models.ForeignKey(User, related_name='proposer', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='申请人')
    approver = models.ForeignKey(User, related_name='approver', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='审批人')
    receiver = models.ForeignKey(User, related_name='receiver', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='接单人')

    class Meta:
        verbose_name = '工单信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class WorkOrderRecord(models.Model):
    type_choices = (('0', '退回'), ('1', "派发"), ('2', "执行"), ('3', "确认"))
    name = models.ForeignKey(User, verbose_name=u"记录人")
    work_order = models.ForeignKey(WorkOrder, verbose_name=u"工单信息")
    record_type = models.CharField(max_length=10, choices=type_choices, verbose_name=u"记录类型")
    content = models.CharField(max_length=500, verbose_name=u"记录内容", default="")
    file_content = models.FileField(upload_to='file/%Y/%m', blank=True, null=True, verbose_name='实施文档')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"记录时间")

    class Meta:
        verbose_name = u"执行记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.record_type
