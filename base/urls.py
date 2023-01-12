from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoint),
    path('advocate/', views.advocate , name="advocate"),
    # path('advocate/<str:username>/', views.advocate_list)
    path('advocate/<str:username>/', views.AdvocatesDetails.as_view())

]