from django.contrib import admin
from .models import News,Category,Tag,Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_at','category')
    list_filter = ('category',)
    search_fields = ('title','content')
    list_per_page = 10


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','news','active')
    list_filter = ('active',)
    search_fields = ('news',)
    list_per_page = 10
    list_editable = ('active',)



admin.site.register(Category)
admin.site.register(Tag)
