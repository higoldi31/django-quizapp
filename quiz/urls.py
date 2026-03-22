from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('question/<int:id>/',views.question_page,name='question'),
    path('results/', views.result_view, name='results'),
]