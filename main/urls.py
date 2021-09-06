from django.urls import path
from  . import views
app_name='main'
urlpatterns = [
    path('',views.DetailView,name='DetailView'),
    path('<slug:c_slug>/', views.DepartmentView, name='DepartmentView'),

]