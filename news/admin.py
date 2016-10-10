#coding=utf-8
from django.contrib import admin
from news import models
from _csv import list_dialects





# Register your models here.

class   NewsDisplay(admin.ModelAdmin):
    list_display =('title','fdate','dep','news_type','author','count',)  #指定要显示的字段
    fields = ('title','fdate','dep','news_type','author','contentUEdite',)   #自定义编辑表单，在编辑表单的时候 显示哪些字段，显示的属性,按顺序排序
    search_fields=('title','dep__department','author')  #搜索ptype是外键，dep__department表示从dep表里取department字段
    list_filter=('title','fdate','dep')  # 过滤器
    

    
class DepDisplay(admin.ModelAdmin):
    list_display = ('department','sort',)
    
    
class NewsTyepDisplay(admin.ModelAdmin):
    list_display = ('name',)    

admin.site.register(models.NewsTyep,NewsTyepDisplay)
admin.site.register(models.Dep,DepDisplay)
admin.site.register(models.News,NewsDisplay)



