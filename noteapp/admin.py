from django.contrib import admin
from noteapp.models import Note, Folder 

class noteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nName', 'nDate', 'folder')
    list_filter = ('nName', 'nDate', 'folder')
    search_fields = ('nName', 'nDate', 'folder')
    ordering = ('id',)

admin.site.register(Note, noteAdmin)  # 註冊 Note 模型
admin.site.register(Folder)  # 註冊 Folder 模型
