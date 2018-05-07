from django.contrib import admin
from .models import *

class HeroInfoInline(admin.TabularInline): # StackedInline /TabularInline  表单/表格 格式
    model = HeroInfo    # 要嵌入的类名
    extra = 3           # 要嵌入的数目


# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 5
    fieldsets = [
        ('basic', {'fields': ['btitle']}),
        ('more', {'fields': ['bpub_date']}),
    ]
    inlines = [HeroInfoInline] # 添加book的时候同时添加 hero


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname']
    list_filter = ['hname']
    search_fields = ['hname']
    list_per_page = 5


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)