from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_change,password_change_done
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^login/$', login, name= 'login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^companies/$', views.companies, name='companies'),
    url(r'^company-add/$', views.company_add, name='company_add'),
    url(r'^users/$', views.users, name='users'),
    url(r'^edit/user/(?P<username>[-\w]+)/$', views.user_edit, name='user_edit'),
    url(r'^edit/company/(?P<company>[-\w]+)/$', views.company_edit, name='company_edit'),
    url(r'^user/(?P<username>[-\w]+)/$', views.user_details, name='user_details'),
    url(r'^company/(?P<slug>[-\w]+)/$',views.company_details,name='company_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
