#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M

import xadmin

from .models import SystemSetup, EmailSetup


class SystemSetupAdmin(object):
    list_display = ['loginTitle', 'mainTitle', 'headTitle', 'copyright', 'url']
    list_filter = ['loginTitle', 'mainTitle', 'headTitle', 'url']


class EmailSetupAdmin(object):
    list_display = ['emailHost', 'emailPort', 'emailUser', 'emailPassword']


xadmin.site.register(SystemSetup, SystemSetupAdmin)
xadmin.site.register(EmailSetup, EmailSetupAdmin)
