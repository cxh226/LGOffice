#coding=utf-8
from django.db import models


# Create your models here.


class NewsTyep(models.Model):
    name =  models.CharField(max_length=30)  #资讯类型
    def __str__(self):    
        return self.name
    
class   Dep(models.Model):
    department =  models.CharField(max_length=255,primary_key=True) #部门
    sort =  models.IntegerField(u'排序')  #排序位置
    
class News(models.Model):
    title = models.CharField(u'标题',max_length=255) #资讯标题
    content =  models.TextField(u'内容')
    create_date =  models.DateField(auto_now_add=True)  #资讯创建时间
    fdate =  models.DateField(u'发布时间') #发布时间
    dep =  models.ForeignKey(Dep)  #部门ID
    news_type =  models.ForeignKey(NewsTyep)  #发布文章的类型
    author =  models.CharField(u'发布人',max_length=20)  #发布人
    count =  models.PositiveIntegerField() #浏览次数,正数
   
    
    
    
    
    
        