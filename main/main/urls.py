from django.contrib import admin
from django.urls import path

from shortener.views import HomeView, MainCBView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path(r'^(?P<shortcode>[\w-]+)/$', MainCBView.as_view(), name = 'scode'),
]
