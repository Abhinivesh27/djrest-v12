from .views import GenericView
from django.urls import path
from .views import home
urlpatterns = [
    path('', home),
    path('api', GenericView.as_view()),
    path('api/<int:id>', GenericView.as_view())
]
