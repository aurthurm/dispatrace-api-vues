from django.conf import settings
from django.db import models
from django.utils import timezone
import os
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from mptt.models import MPTTModel, TreeForeignKey
from apps.memos.settings import ATTACHMENT_UPLOAD_TO

class AbstractComment(MPTTModel):
    """
        Comment Abstract model
    """
    parent = TreeForeignKey(
        'self', 
        related_name='%(class)s_sub_comment', 
        db_index=True, 
        null=True, 
        blank=True, 
        on_delete=models.PROTECT
    )
    comment = models.TextField()
    commenter = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT
    )
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment

    class Meta:
        get_latest_by = ['timestamp']
        abstract=True

class AbstractAttachment(MPTTModel):
    """
        Attachment Abstract model
    """
    parent = TreeForeignKey(
        'self', 
        related_name='%(class)s_file_attachment', 
        db_index=True, 
        null=True, 
        blank=True, 
        on_delete=models.PROTECT
    )

    def file_upload_to_dispatcher(self, entry, filename):
        return entry.file_upload_to(filename)

    def file_upload_to(self, filename):
        now = timezone.now()
        filename, extension = os.path.splitext(filename)

        return os.path.join(
                ATTACHMENT_UPLOAD_TO,
                now.strftime('%Y'),
                now.strftime('%m'),
                now.strftime('%d'),
                '%s%s' % (slugify(filename), extension)
            )

    file_name = models.CharField(
        _('file name'),
        max_length=255
    )

    file = models.FileField(
        _('file'), blank=True,
        upload_to=file_upload_to_dispatcher,
        help_text=_('Attach File'))

    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        get_latest_by = ['timestamp']
        abstract=True
