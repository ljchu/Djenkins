from django.conf.urls import patterns, url

urlpatterns = patterns('UserContacts.views',
    url(r'^$', 'home'),
    url(r'all$', 'all_contacts'),
)
