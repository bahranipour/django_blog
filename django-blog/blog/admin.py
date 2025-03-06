from django.contrib import admin
from .models import Post,Category,Tag,Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_at','category')
    list_filter = ('category','tags')
    search_fields = ('title','content')
    list_per_page = 10

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','post','active')
    list_filter = ('active',)
    search_fields = ('post',)
    list_per_page = 10
    list_editable = ('active',)
    
admin.site.register(Category)
admin.site.register(Tag)

