"""dpcrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from mydpcrm import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/v1/rest-auth/', include('rest_auth.urls')),

    url(r'^api/v1/rest-auth/leadcreate/$', views.NewLeadsCreateOrGet.as_view()),
    url(r'^api/v1/rest-auth/leadupdate/(?P<pk>[0-9]+)/$', views.UpdateLeadsOrGet.as_view()),

    url(r'^api/v1/rest-auth/coldleadcreate/$', views.NewColdLeadsCreateOrGet.as_view()),
    url(r'^api/v1/rest-auth/coldleadupdate/(?P<pk>[0-9]+)/$', views.UpdateColdLeadsOrGet.as_view()),

    url(r'^api/v1/rest-auth/referralleadcreate/$', views.ReferralLeadsCreateOrGet.as_view()),
    url(r'^api/v1/rest-auth/referralleadupdate/(?P<pk>[0-9]+)/$', views.UpdateReferralLeadsOrGet.as_view()),

    url(r'^api/v1/rest-auth/scheduledleadcreate/$', views.ScheduledLeadsCreateOrGet.as_view()),
    url(r'^api/v1/rest-auth/scheduleleadupdate/(?P<pk>[0-9]+)/$', views.UpdateScheduledLeadsOrGet.as_view()),

    url(r'^api/v1/rest-auth/convertedleadcreate/$', views.ConvertedLeadsCreateOrGet.as_view()),
    url(r'^api/v1/rest-auth/convertedleadupdate/(?P<pk>[0-9]+)/$', views.UpdateConvertedLeadsOrGet.as_view()),

    url(r'^api/v1/rest-auth/leadnotecreate/$', views.LeadNotesCreateOrGet.as_view()),
    url(r'^api/v1/rest-auth/leadnoteupdate/(?P<pk>[0-9]+)/$', views.UpdateLeadNotesOrGet.as_view()),

    url(r'^api/v1/rest-auth/referralnotecreate/$', views.ReferralNotesCreateOrGet.as_view()),
    url(r'^api/v1/rest-auth/referralnoteupdate/(?P<pk>[0-9]+)/$', views.UpdateReferralNotesOrGet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)