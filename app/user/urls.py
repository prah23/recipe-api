<<<<<<< HEAD
from django.urls import path
=======
from django.urls import path, include
>>>>>>> 2d8c01bf7c345e1c15db16ef9f0185aaded44b84
from user import views


app_name = 'user'

urlpatterns = [
<<<<<<< HEAD
    path('create/', views.CreateUserView.as_view(), name='create'),
]
=======
    path('create/',views.CreateUserView.as_view(),name='create'),
]
>>>>>>> 2d8c01bf7c345e1c15db16ef9f0185aaded44b84
