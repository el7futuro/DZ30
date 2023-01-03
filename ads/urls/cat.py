from django.urls import path
from ads import views
from ads.views import CategoryDetailView, CatListCreateView

urlpatterns = [
    path('', CatListCreateView.as_view()),
    path('<int:pk>', CategoryDetailView.as_view())


]