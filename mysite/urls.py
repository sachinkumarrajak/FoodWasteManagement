from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views as core_views


urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home, name='home'),
	url(r'^add/new/$', core_views.addnew, name='addnew'),
	url(r'^add/orphanage-details/$', core_views.addorphan, name='addorphan'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^login/agent/$', auth_views.login, {'template_name': 'login.html'}, name='agentlogin'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^signup/agent/$', core_views.signupag, name='signupag'),
    url(r'^update/(?P<pk>\d+)$', core_views.updates, name='update_det'),
    url(r'^delete/(?P<pk>\d+)$', core_views.deletes, name='delete_det'),
    url(r'^updateorp/(?P<pk>\d+)$', core_views.updateorp, name='update_orp_det'),
    url(r'^deleteorp/(?P<pk>\d+)$', core_views.deleteorp, name='delete_orp_det'),
    url(r'^orphanage/$', core_views.orphangaedets, name='orphanagedet'),
	url(r'^allocate/(?P<pk>\d+)$',core_views.allocatedet, name='allocate_dets'),
	url(r'^architecture/$',core_views.archi,name='archi'),
    url(r'^charts/(?:(?P<chart_type>.+))?/(?:(?P<cha_type>.+))?/$',core_views.chartsview,name='charts'),
	
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
