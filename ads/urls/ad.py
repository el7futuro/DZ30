from django.urls import path
from ads import views
from ads.views import AdDetailView, AdListCreateView

urlpatterns = [
    path('', AdListCreateView.as_view()),
    path('<int:pk>', AdDetailView.as_view())


]