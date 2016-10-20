#coding=utf-8#

from django.db import models

import django.utils.timezone as timezone
# Create your models here.


class VideoType(models.Model):
    name = models.CharField(u'视频类型',max_length=255)
    
    class Meta:
        verbose_name = u'视频类型'
        verbose_name_plural = verbose_name
    
    def   __str__(self):
        return self.name
    
class VideoUpdate(models.Model):
    name = models.CharField(u'视频名称',max_length=255)
    title = models.CharField(u'视频标题',max_length=255)
    img = models.ImageField(u'图片',upload_to = 'img')
    detail = models.TextField(u'视频筒介',blank=True,null=True)
    videotype = models.ForeignKey(VideoType,verbose_name='视频类型',default=2)
    speaker = models.CharField(u'主讲人',max_length=255,blank=True,null=True)
    playcount = models.IntegerField(u'播放数',default=0)
    videolength = models.CharField(u'视频时间',max_length=255)
    createdate = models.DateField(u'创建时间',auto_now_add = True)
    uploaddate = models.DateField(u'上传时间',auto_now =True)
    uploaduser = models.CharField(u'上传用户',max_length = 255)
    
    class Meta:
        verbose_name = u'视频上传'
        verbose_name_plural = verbose_name
     
    def __str__(self):
         return self.title   
     
     
     
    


        

