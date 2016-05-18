from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from member.views import *
from member.forms import *

create_member_forms = (
    ('basic_info', ClientBasicInformation),
    ('address_information', ClientAddressInformation),
    ('referent_information', ClientReferentInformation),
    ('payment_information', ClientPaymentInformation),
    ('dietary_restriction', ClientRestrictionsInformation),
    ('emergency_contact', ClientEmergencyContactInformation),
)

member_wizard = ClientWizard.as_view(create_member_forms,
                                     url_name='member:member_step')

urlpatterns = patterns('',
                       url(r'^create/$', member_wizard, name='member_step'),
                       url(r'^create/(?P<step>.+)/$', member_wizard,
                           name='member_step'),
                       url(_(r'^list/$'), ClientList.as_view(), name='list'),
                       url(_(r'^notes/$'), NoteList.as_view(), name='notes')
                       )
