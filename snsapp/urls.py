from django.urls import path

from .views import IndexView, Page1View, Page2View

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('page1/', Page1View.as_view(), name='page1'),
    path('page2/', Page2View.as_view(), name='page2'),
]