#coding=utf-8
from django.contrib import admin
from news import models
from _csv import list_dialects

# Register your models here.

class   NewsDisplay(admin.ModelAdmin):
    list_display =('title','fdate','dep','news_type','author','count',)  #指定要显示的字段
    fields = ('title','fdate','dep','news_type','author','content',)   #自定义编辑表单，在编辑表单的时候 显示哪些字段，显示的属性
    
class DepDisplay(admin.ModelAdmin):
    list_display = ('department','sort',)

admin.site.register(models.NewsTyep)
admin.site.register(models.Dep,DepDisplay)
admin.site.register(models.News,NewsDisplay)

