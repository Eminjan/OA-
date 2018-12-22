#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M

import json
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.conf import settings

from utils.mixin_utils import LoginRequiredMixin
from rbac.models import Menu
from .models import SystemSetup
from .forms import SystemSetupForm

# Create your views here.

class SystemView(LoginRequiredMixin, View):
    """
    系统模块入口
    """
    def get(self, request):
        return render(request, 'system/system_index.html')


class SystemSetupView(LoginRequiredMixin, View):
    """
    系统基本配置：create
    """

    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'system/tools/system-setup.html', ret)

    def post(self, request):
        res = dict(result=False)
        system_setup_form = SystemSetupForm(request.POST)
        if system_setup_form.is_valid():
            system_setup_form.save()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')


class EmailSetupView(LoginRequiredMixin, View):
    """
    发件邮箱设置：create
    """

    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'system/tools/email-setup.html', ret)