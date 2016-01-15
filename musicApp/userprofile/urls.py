from django.conf.urls import url
from userprofile import views

urlpatterns = [
	url(r'^logout/',views.logout_view,name="logout"),
]