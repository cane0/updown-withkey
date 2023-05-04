from django.urls import path
from .views import up_img_view, home

urlpatterns = [
    path('', home, name='home'),
    path('upload/', up_img_view, name='upload-image'),
]