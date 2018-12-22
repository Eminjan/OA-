#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M

import xadmin
from xadmin import views

from .models import Menu, Role


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True #调用更多主题


class GlobalSettings(object):
    site_title = "NEO协同办公平台后台管理系统"
    site_footer = "Copyright © 2018 NEO. Version1.0.0"
    menu_style = "accordion"


class MenuAdmin(object):
    list_display = ['id', 'title', 'is_top', 'icon', 'code', 'url', 'parent']
    list_filter = ['id', 'title', 'is_top', 'icon', 'code', 'parent']
    list_editable = ['is_top', 'url']





class RoleAdmin(object):
    list_display = ['id', 'title', 'permissions']


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(Menu, MenuAdmin)
xadmin.site.register(Role, RoleAdmin)

