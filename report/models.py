#coding=utf-8#

from django.db import models
import django.utils.timezone as timezone
import LGOffice.settings 

from news.models import  Dep



from django.db.models.functions import Length
from django.template.defaultfilters import default

import django.db.models.deletion



class ReportUpdata(models.Model):
    depid  = models.ForeignKey(Dep,verbose_name='上传部门',on_delete=b'SET_NULL')  #blank=True  允许没有数据, null=True 允许值为null
    username = models.CharField(u'上传用户',max_length=255)

    title = models.CharField(u'标题',max_length=255)
    updatafile1 = models.FileField(u'工作报告1',max_length=256)
    updatafile2 = models.FileField(u'工作报告2',upload_to='uploads/%Y/%m/',max_length=256,blank  = True)
    updatafile3 = models.FileField(u'工作报告3',upload_to='uploads/%Y/%m/',max_length=256 ,blank  = True)
    updatafile4 = models.FileField(u'工作报告4',upload_to='uploads/%Y/%m/',max_length=256 ,blank  = True)
    updatafile5 = models.FileField(u'工作报告5',upload_to='uploads/%Y/%m/',max_length=256,blank  = True)

    createdata = models.DateField(u'创建日期',auto_now_add=True) #创始日期，更新时不会变
    updata = models.DateField(u'上传日期',auto_now=True) #每当该对象使用save()时，该字段的值就会被更新。
    
    class Meta:
        verbose_name = u'工作报告上传'
        verbose_name_plural = verbose_name
        

    def   __str__(self):
        return self.depid.department

