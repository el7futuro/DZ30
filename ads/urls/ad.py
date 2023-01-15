from django.urls import path


from ads.views.ad import AdListView, AdDetailView, AdUpdateView, AdDeleteView, AdImageUpdate


urlpatterns = [


    path('ad/', AdListView.as_view(), name='AdListView'),
    path('ad/<int:pk>', AdDetailView.as_view(), name='AdDetailView'),
    path('ad/<int:pk>/update', AdUpdateView.as_view()),
    path('ad/<int:pk>/delete', AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', AdImageUpdate.as_view())

]

