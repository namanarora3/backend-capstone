from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.UploadFileView.as_view(), name='upload_file'),
    path('files/', views.GetFileListView.as_view(), name='get_file_list'),
    path('files/<int:pk>/', views.GetFileView.as_view(), name='get_file'),
]
