from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee-list'),
    path('new/', views.EmployeeCreateView.as_view(), name='employee-create'),
    path('<str:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('<str:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee-update'),
    path('<str:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee-delete'),
]