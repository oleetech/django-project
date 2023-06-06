from django.urls import path
from . import views
urlpatterns = [
    path('',views.post_list,name='home'),
    path('<slug:slug>/',views.post_detail,name='post_detail'),
    
    path('<slug:slug>/comment/', views.create_comment, name='comment_create')
]