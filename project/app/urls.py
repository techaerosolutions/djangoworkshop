from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('detail/',views.detail,name='detail'),
    path('addproduct/',views.addproduct,name="addproduct")

]