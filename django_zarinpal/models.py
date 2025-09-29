import jdatetime
from django.db import models
from django.utils.translation import gettext_lazy as _

class TransactionStatus(models.IntegerChoices):
    PENDING = 0, _("Pending")
    PAID = 1, _("Paid")
    FAILED = 2, _("Failed")


class Transaction(models.Model):

    amount = models.PositiveBigIntegerField(_("Amount"))
    authority = models.CharField(_("Authority"), max_length=64, null=True, blank=True, db_index=True)
    ref_id = models.CharField(_("Reference ID"), max_length=255, null=True, blank=True, db_index=True)
    status = models.PositiveSmallIntegerField(
        _("Status"), choices=TransactionStatus.choices, default=TransactionStatus.PENDING
    )
    created_at = models.DateTimeField(_("request time"),auto_now_add=True)
    verified_at = models.DateTimeField(_("Verified At"), null=True, blank=True)

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.id}"

    def to_jalali(self, dt):
        return jdatetime.datetime.fromgregorian(datetime=dt) if dt else None

    @property
    def created_at_jalali(self):
        return self.to_jalali(self.created_at)
    
    def get_created_at_jalali_display(self):
        return self.created_at_jalali.strftime("%Y/%m/%d %H:%M:%S")

    @property
    def verified_at_jalali(self):
        return self.to_jalali(self.verified_at)
    
    def get_verified_at_jalali_display(self):
        return self.verified_at_jalali.strftime("%Y/%m/%d %H:%M:%S")
