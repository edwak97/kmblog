from django.contrib import admin
from .models import NoteRecord, NoteComment

# Register your models here.

#they say it can be replaced with:
#@admin.register(NoteRecord.NoteRecordAdmin)
class NoteRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'header', 'body', 'access_show', 'access_comment']
    list_editable = ['header', 'body']

admin.site.register(NoteRecord, NoteRecordAdmin)
admin.site.register(NoteComment)

