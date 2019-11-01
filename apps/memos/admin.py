from django.contrib import admin
from .models import Memo, MemoComment, MemoAttachment

class AttachmentInline(admin.TabularInline):
    model = MemoAttachment

class CommentInline(admin.TabularInline):
    model = MemoComment

class MemoAdmin(admin.ModelAdmin):

    inlines = [
        AttachmentInline,
        CommentInline
    ]

    list_display = [
        'reference_number',
        'sender',
        'to',
        'subject',
        'created',
        'is_open',
        'accesibility',
        'sent'
    ]

admin.site.register(Memo, MemoAdmin)