from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from apps.accounts.models import *

class Base(models.Model):
	title = models.CharField(max_length = 50)
	creator = models.ForeignKey('auth.User', on_delete = models.PROTECT)
	created = models.DateTimeField(default = timezone.now)

	class Meta:
		abstract = True

	def __str__(self):
		return self.title

class Category(Base):

	# def get_absolute_url(self):
	# 	return reverse('notice:notice-categories')
	pass

class Notice(Base):
	"""
		Notice Model
        Each notice beongs to a category
	"""    
	V_URGENT = 'Urgent'
	MODERATE = 'Moderate'
	NORMAL = 'Normal'
	CHOICES = (
		(V_URGENT, _('Urgent')),
		(MODERATE, _('Moderate')),
		(NORMAL, _('Normal')),
	)

	city = models.ForeignKey(
		City,
		null=True,
		blank=True,
		on_delete=models.PROTECT,
		default=''
	)
	office = models.ForeignKey(
		Office,
		null=True,
		blank=True,
		on_delete=models.PROTECT,
		default=''
	)
	department = models.ForeignKey(
		Department,
		null=True,
		blank=True,
		on_delete=models.PROTECT,
		default=''
	)

	priority = models.CharField(
		_('priority'),
		max_length=15,
		choices=CHOICES,
		default=NORMAL
	)

	description = models.TextField(blank = False)
	category = models.ForeignKey(Category, related_name ="%(class)s_categories", on_delete = models.PROTECT)
	expiry = models.DateTimeField(default = timezone.now)
		
	class Meta:
		ordering = ['-created']
