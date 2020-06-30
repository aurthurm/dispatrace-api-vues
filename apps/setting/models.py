from django.db import models
from django.utils.translation import ugettext_lazy as _

class Preference(models.Model):
    memo_serial_commenting = models.BooleanField(
        _('Enforce Memorandum Serial Commenting'),
        default=True
    )
    action_reauth = models.BooleanField(
        _('Enforce action re-authentication'),
        default=True
    )

    def __str__(self):
        return 'Site Settings'
