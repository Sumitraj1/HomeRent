from django.urls import include, path, re_path
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView


admin.site.site_header = "Rental Admin"
admin.site.site_title = "Rental Admin Portal"
admin.site.index_title = "Welcome to Rental Admin Portal"

admin.autodiscover()
urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/index/')),
    url(r'^index/',views.index),
    url(r'^home/',views.home),
	url(r'^contact/', views.contact),
    url(r'^about/',views.about),
	url(r'^admin/',admin.site.urls),
    url(r'^user/',include('user.urls')),
    url(r'^register', views.register),
    url(r'^login', views.login_view),
    url(r'^profile/',views.profile),
    url(r'^post/$', views.post),
    url(r'^posth/$', views.posth),
    url(r'^logout', LogoutView.as_view()),
    url(r'^descr/',views.descr),
    url(r'^deleter', views.deleter),
    url(r'^deleteh', views.deleteh),
    url(r'^search/', views.search)
]

urlpatterns+= staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)