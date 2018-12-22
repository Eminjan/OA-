#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M

from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

