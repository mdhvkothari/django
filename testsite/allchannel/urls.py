from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^entertainment/$',views.detail),
    url(r'^motivational/$',views.moti),
    url(r'^tech/$',views.tech_person),

]
