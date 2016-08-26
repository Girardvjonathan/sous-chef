from django.db import models
from django.utils.translation import ugettext_lazy as _

from .address import Address
from .contact import Contact

class Member(models.Model):

    class Meta:
        verbose_name_plural = _('members')

    # Member information
    firstname = models.CharField(
        max_length=50,
        verbose_name=_('firstname')
    )

    lastname = models.CharField(
        max_length=50,
        verbose_name=_('lastname')
    )

    address = models.ForeignKey(
        Address,
        verbose_name=_('address'),
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)

    @property
    def home_phone(self):
        try:
            return self.member_contact.filter(type=Contact.HOME).first().value
        except:
            return ""

    @property
    def cell_phone(self):
        try:
            return self.member_contact.all().filter(type=Contact.CELL).first().value
        except:
            return ""

    @property
    def work_phone(self):
        try:
            return self.member_contact.all().filter(type=Contact.WORK).first().value
        except:
            return ""

    @property
    def email(self):
        try:
            return self.member_contact.all().filter(type=Contact.EMAIL).first().value
        except:
            return ""