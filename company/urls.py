from django.urls import path
from .views import CompanyCreateView,CompanyUpdateView, EmployeeUpdateView, employeeList, export_pdf
urlpatterns = [
    path('' , CompanyCreateView.as_view()),
    path('company/<int:pk>' , CompanyUpdateView.as_view()),
    path('employee/<int:pk>' , EmployeeUpdateView.as_view()),
    # path('employee-list/(?companyID={{company.id}})', employeeList),
    path('employee-list', employeeList),
    path('export-pdf', export_pdf),
]

        
