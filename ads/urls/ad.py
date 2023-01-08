from django.urls import path


from ads.views.ad import AdsView, AdsViewDetail, AdUpadeteView, AdDeleteView, AdUploadImageView


urlpatterns = [


    path('ad/', AdsView.as_view(), name='AdsView'),
    path('ad/<int:pk>', AdsViewDetail.as_view(), name='AdsViewDetail'),
    path('ad/<int:pk>/update', AdUpadeteView.as_view()),
    path('ad/<int:pk>/delete', AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', AdUploadImageView.as_view())

]