from django.urls import path, include
from contact import views

urlpatterns = [
    path("", include('contact.urls'))
]
