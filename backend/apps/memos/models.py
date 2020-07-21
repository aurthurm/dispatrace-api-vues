from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
import os
from rest_framework import reverse as api_reverse

from apps.shared import AbstractComment, AbstractAttachment

class Core(models.Model):
    """
		Fields to determine our recipients and base details
	"""
    recipients = models.ManyToManyField(
        User,
        related_name="%(class)s_recipients"
    )
    to = models.ForeignKey(
        User,
        related_name="%(class)s_to",
        null=True,
        blank=True,
        default='',
        on_delete=models.PROTECT
    )
    sender = models.ForeignKey(
        User,
        related_name="%(class)s_from",
        on_delete=models.PROTECT
    )
    is_open = models.BooleanField( # is open for commenting ?
        _('is open'),
        default=True
    )
    archived = models.BooleanField(
        _('archived'),
        default=False
    )
    sent = models.BooleanField(
        _('sent'),
        default=False
    )
    created = models.DateTimeField(
        _('date created'), 
        default=timezone.now
    )
    date_sent = models.DateTimeField(
        _('date sent'), 
        db_index=True, 
        null=True,
        blank=True
    )
    reference_number = models.CharField(
        _('reference number'),
        max_length=23,
        db_index=True, 
        unique=True
    )

    class Meta:
        abstract=True
        get_latest_by = 'created'

class Content(models.Model):
    """
        Field to write content for the Memo: Reason and body message
    """
    subject = models.CharField(
        _('subject'),
        max_length=255
    )
    slug = models.SlugField(
        _('slug'), 
        max_length=255, 
        blank=True
    )
    message = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject)
        super(Content, self).save(*args, **kwargs)

    def __str__(self):
        return self.subject

    class Meta:
        abstract=True

PUBLIC = 'PUB'
PRIVATE = 'PVT'
CHOICES = (
    (PUBLIC, _('Public')),
    (PRIVATE, _('Private')),
)

class Accesibility(models.Model):
    """
        Determines whether the memo being created is public or private.
        Public Memos are seen by everyone. 
        Private Memos are seen only by the sender and selected recipinet(s)
    """
    accesibility = models.CharField(
        _('memo type'),
        max_length=10,
        choices=CHOICES,
        default=PUBLIC
    )

    class Meta:
        abstract=True


V_URGENT = 'Very Urgent'
MODERATE = 'Moderate'
NORMAL = 'Normal'
CHOICES = (
    (V_URGENT, _('Very Urgent')),
    (MODERATE, _('Moderate')),
    (NORMAL, _('Normal')),
)

class Priority(models.Model):
    """
        Determines whether the memo being created is public or private.
        Public Memos are seen by everyone. 
        Private Memos are seen only by the sender and selected recipinet(s)
    """
    mem_priority = models.CharField(
        _('memo priority'),
        max_length=15,
        choices=CHOICES,
        default=NORMAL
    )

    class Meta:
        abstract=True

class Memo(
        Core, 
        Priority,
        Accesibility,
        Content,
    ):
    """
        Memo Model
    """

    commenting_required = models.BooleanField(
        _('commenting required'),
        default=True
    )

    receptors = models.ManyToManyField( # for memos that do not  need commenting. A user who acknwledged reception will be added here
        User,
        related_name="%(class)s_receptors",
        blank=True
    )

    def get_api_url(self):
        return reverse('dispatrace-api:memo-retrieveupdate', kwargs={'pk': self.pk})
    
    @property
    def owner(self):
        return self.user

    class Meta:
        ordering = ['-created']
        verbose_name = _('memorandum')
        verbose_name_plural = _('memorandums')
        permissions = (
            ('add_comment', 'Comment Memo'), 
        )


class Archive(models.Model):
    """
        Close Memo / Archive
    """
    memo = models.ForeignKey(
        Memo,
        on_delete=models.PROTECT
    )
    archived = models.BooleanField(
        _('archived'),
        default=False
    )
    archiver = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    date_archived = models.DateTimeField(
        _('date archived'), 
        db_index=True, 
        default=timezone.now
    )

    def __str__(self):
        return str(self.memo.subject)

    class Meta:
        verbose_name = _('archive')
        verbose_name_plural = _('archives')


class MinMaxFloat(models.FloatField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)  


class MemoComment(AbstractComment):
    """
        Add Comments to memo
    """
    memo = models.ForeignKey(
        Memo, 
        related_name='%(class)s_comment', 
        on_delete=models.PROTECT
    )
    
    class Meta:
        get_latest_by = ['timestamp']
        verbose_name = _('memo comment')
        verbose_name_plural = _('memo comments')


class MemoAttachment(AbstractAttachment):
    """
        Add Attachments to memo
    """
    memo = models.ForeignKey(
        Memo, 
        related_name='%(class)s_attachment', 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "Attached to: " + str(self.memo)

