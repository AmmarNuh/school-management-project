from django.contrib import admin
from django.urls import path, re_path
from . import views


app_name = 'schDetails'

urlpatterns = [ 
               # ---------------- Schools related ---------------- #

    path('schoolDetails/<int:pk>/', views.SchoolDetailView.as_view(), name='details'),
    path('list/', views.SchoolListView.as_view(), name='list'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='delete'),

                # ---------------- Students related ---------------- #

    path('studentsDetails/<int:pk>/', views.StudentDetailView.as_view(), name='stuDetails'),
    path('listst/', views.StudentListView.as_view(), name='listst'),
    path('createstudent/', views.StudentCreateView.as_view(), name='createstudent'),
    path('updatest/<int:pk>/', views.StudentUpdateView.as_view(), name='updatest'),
    path('deletest/<int:pk>/', views.StudentDeleteView.as_view(), name='deletest'),
    



    # path('details', views.index, name='details'),

]
