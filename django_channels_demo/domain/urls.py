from django.urls import path

from .views import CoordinatesAPIView


urlpatterns = [
    path(
        'coordinates/',
        view=CoordinatesAPIView.as_view({'get':'list', 'post':'create'}),
        name='coordinates'
    ),
    path(
        'coordinates/<int:id>', 
        view=CoordinatesAPIView.as_view({'get':'retrieve'}),
        name='coordinate-detail'
    )
]