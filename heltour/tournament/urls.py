"""heltour2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from . import views, api

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^season/$', views.season_landing, name='season_landing'),
    url(r'^season/(?P<season_id>[0-9]+)/$', views.season_landing, name='season_landing_by_season'),
    url(r'^register/$', views.register, name='register'),
    url(r'^season/(?P<season_id>[0-9]+)/register/$', views.register, name='register_by_season'),
    url(r'^registration_success/$', views.registration_success, name='registration_success'),
    url(r'^registration_closed/$', views.registration_closed, name='registration_closed'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^season/(?P<season_id>[0-9]+)/faq/$', views.faq, name='faq_by_season'),
    url(r'^rosters/$', views.rosters, name='rosters'),
    url(r'^season/(?P<season_id>[0-9]+)/rosters/$', views.rosters, name='rosters_by_season'),
    url(r'^standings/$', views.standings, name='standings'),
    url(r'^season/(?P<season_id>[0-9]+)/standings/$', views.standings, name='standings_by_season'),
    url(r'^crosstable/$', views.crosstable, name='crosstable'),
    url(r'^season/(?P<season_id>[0-9]+)/crosstable/$', views.crosstable, name='crosstable_by_season'),
    url(r'^pairings/$', views.pairings, name='pairings'),
    url(r'^round/(?P<round_number>[0-9]+)/pairings/$', views.pairings, name='pairings_by_round'),
    url(r'^season/(?P<season_id>[0-9]+)/pairings/$', views.pairings, name='pairings_by_season'),
    url(r'^season/(?P<season_id>[0-9]+)/round/(?P<round_number>[0-9]+)/pairings/$', views.pairings, name='pairings_by_season_round'),
    url(r'^stats/$', views.stats, name='stats'),
    url(r'^season/(?P<season_id>[0-9]+)/stats/$', views.stats, name='stats_by_season'),
    url(r'^api/find_pairing/$', api.find_pairing, name='api_find_pairing'),
    url(r'^api/update_pairing/$', api.update_pairing, name='api_update_pairing'),
]
