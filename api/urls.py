from django.urls import path
from . import view,views

app_name = "api"

urlpatterns = [
    path('adduser/',view.adduser),
    path('service_state',views.service_state,name="service_state"),
]
