#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M
import re

from django import forms
from .models import SystemSetup


class SystemSetupForm(forms.ModelForm):
    class Meta:
        model = SystemSetup
        fields = '__all__'