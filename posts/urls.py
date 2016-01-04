from django.conf.urls import url
from posts import views
urlpatterns = [
    url(r'^$', views.showPosts, name="home"),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^add/$', views.addPost, name="add_post"),
    url(r'^login/$', views.login_me, name="login"),
    url(r'^logout/$', views.logout_me, name="logout_me"),
    url(r'^edit/(?P<id>[0-9]+)/$', views.editPost, name="edit_post"),
    url(r'^(?P<id>[0-9]+)/$', views.showPost, name="post"),
    url(r'^delete/(?P<id>[0-9]+)/$', views.deletePost, name="delete_post"),

]