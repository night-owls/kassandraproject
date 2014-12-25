__author__ = 'cemkiy'
__author__ = 'barisariburnu'

from django.conf.urls import patterns, url
from member import views
import django.contrib.auth

urlpatterns = patterns('',
                        url(r'^new_member/$', 'member.views.new_member'),
                        url(r'^member_profile/$', 'member.views.member_profile'),
                        url(r'^payment_page/$', 'member.views.payment_page'),
                        url(r'^succes_url/$', 'member.views.success_url'),
                        )