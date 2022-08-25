from django.urls import path
from trans.views import HomeView

app_name = 'trans'

urlpatterns = [
    path('',HomeView.as_view(),name='home')
]