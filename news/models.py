#encoding=utf-8
from django.db import models
from DjangoUeditor.models import UEditorField
import sys
reload(sys)






# Create your models here.


class NewsTyep(models.Model):
    name =  models.CharField(max_length=30)  #资讯类型
    
 #重写Meta模块,修改在管理后台中的显示名称      
    class Meta:
        verbose_name = u'文章类型'
        verbose_name_plural = u'文章类型'
        app_label = u"news"
        #按名称排序  


    
class   Dep(models.Model):
    department =  models.CharField(max_length=255,primary_key=True) #部门
    sort =  models.IntegerField(u'排序')  #排序位置    
 #重写Meta模块,修改在管理后台中的显示名称      
    class Meta:
        verbose_name = u'部门'
        verbose_name_plural = u'部门'
        app_label = u"news"
        db_table = u'Dep'
        #按名称排序  
        ordering = ['sort']  
    
class News(models.Model):
    title = models.CharField(u'标题',max_length=255) #资讯标题
    create_date =  models.DateField(auto_now_add=True)  #资讯创建时间
    fdate =  models.DateField(u'发布时间') #发布时间
    dep =  models.ForeignKey(Dep)  #部门ID
    news_type =  models.ForeignKey(NewsTyep)  #发布文章的类型
    author =  models.CharField(u'发布人',max_length=20)  #发布人
    count =  models.PositiveIntegerField() #浏览次数,正数
    contentUEdite=UEditorField(u'发布内容 ',width=1200, height=300, toolbars="full", imagePath="", filePath="upload/", upload_settings={"imageMaxSize":1204000},settings={},command=None,blank=True)
#     last_login_ip=models.IPAddressField() #发布电脑的IP  
    
 #重写Meta模块,修改在管理后台中的显示名称      
    class Meta:
        verbose_name = u'发布文章'  #修改从管理级'发布文章'进入后的页面显示，显示为'发布文章'
        verbose_name_plural = u'发布文章'  #修改管理级页面显示
        app_label = u"news"    
    
    
    
        