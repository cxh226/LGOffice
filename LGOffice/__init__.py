#coding=utf-8
import pymysql
from django.contrib import admin
pymysql.install_as_MySQLdb()


default_app_config = 'LGOffice.apps.RockNRollConfig'


admin.site.site_header = '乐歌办公系统管理后台'
admin.site.site_title = '乐歌办公系统'
