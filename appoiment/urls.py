from django.urls import path
from . import views

app_name = 'appoiment'

urlpatterns = [
    path("<slug:c_slug>/<slug:doc_slug>/", views.DocDetails, name='DocDetails'),
    path("FormDetail", views.FormDetail, name='FormDetail'),



]
