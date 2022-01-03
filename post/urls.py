from django.urls import path
from basic import views
from .views import QueryingTheDBView

urlpatterns = [
    path('queries/', QueryingTheDBView.as_view(), name='queries')
]
