from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):

    list_display = ['id','title','date','views','image']
    list_display_links = ['id','title']
    list_filter = ['date','views']

class CommentAdmin(admin.ModelAdmin):

    list_display = ['id','name','content','date','show_comment','show_comment_label']
    list_display_filter = ['date','show_comment','show_comment_label']


admin.site.register(models.Login)
admin.site.register(models.slider)
admin.site.register(models.posts,PostAdmin)
admin.site.register(models.comments,CommentAdmin)
admin.site.register(models.FilterComments)
admin.site.register(models.logs)
admin.site.register(models.comments_replays)