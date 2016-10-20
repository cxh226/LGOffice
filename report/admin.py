from django.contrib import admin
from report import models

# Register your models here.



class ReportUpdataDisplay(admin.ModelAdmin):
    list_display = ('depid','username','title','updatafile1','updata')

    

admin.site.register(models.ReportUpdata,ReportUpdataDisplay)
