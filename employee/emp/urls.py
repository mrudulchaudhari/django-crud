from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee-list'),
    path('employee/<int:employee_id>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee/new/', views.EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/<int:employee_id>/edit/', views.EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/<int:employee_id>/delete/', views.EmployeeDeleteView.as_view(), name='employee-delete'),
]