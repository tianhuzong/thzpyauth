from django.urls import path
from . import view,views
urlpatterns = [
    path('adduser/',view.adduser),
    path('service_state',views.service_state,name="service_state"),
]
