from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

app_name='accounts'

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^login/$',login,{'template_name':'accounts/login.html'}),
    url(r'^logout/$',logout,{'template_name':'accounts/logout.html'}),
    url(r'^register/$',views.register,name='register'),
    url(r'^entertainment/(?P<slug>[\w-]+)/$',views.person_detail,name='detail'),
    url(r'^motivational/(?P<slug>[\w-]+)/$',views.moti_detail,name='moti'),
    url(r'^tech/(?P<slug>[\w-]+)/$',views.tech_detail,name='tech'),    
]
