#coding=utf-8
from django import forms
from .models import *

#查询道具获取途径时收集所查道具名称的表单，有两种输入模式，一种是手工输入，另一种是提供全部道具的下拉列表
import logging
from django.forms import ModelChoiceField

class PaModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.pa_name

class EaModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.ea_name

class SnModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.cn_name

class PropertyNameForm(forms.Form):
    manual_input = PaModelChoiceField(label='或者从本下拉列表中选择', queryset=Property.objects.all(),to_field_name='pa_name')


class EquipNameForm(forms.Form):
    select_input = EaModelChoiceField(label='本下拉列表中选择', queryset=Equip.objects.all(),to_field_name='ea_name')

class SceneNameForm(forms.Form):
    select_input = SnModelChoiceField(label='本下拉列表中选择', queryset=Scenename.objects.all(),to_field_name='cn_name')



