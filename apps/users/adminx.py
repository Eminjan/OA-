#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M
import xadmin

from .models import Structure


class StructureAdmin(object):
    list_display = ['title', 'type', 'parent']
    list_filter = ['title', 'type', 'parent']

xadmin.site.register(Structure, StructureAdmin)

