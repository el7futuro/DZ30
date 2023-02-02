from django.urls import path
from rest_framework import routers
from ads.views.sel import SelectionListView, SelectionRetrieveView, SelectionCreateView, SelectionUpdateView, \
    SelectionDeleteView

# router = routers.SimpleRouter()
# router.register('sel', SelectionListView, basename='Selection')

urlpatterns = [path('selection/', SelectionListView.as_view()),
               path('selection/<int:pk>/', SelectionRetrieveView.as_view()),
               path('selection/create/', SelectionCreateView.as_view()),
               path('selection/<int:pk>/update/', SelectionUpdateView.as_view()),
               path('selection/<int:pk>/delete/', SelectionDeleteView.as_view())]

# urlpatterns += router.urls
#
