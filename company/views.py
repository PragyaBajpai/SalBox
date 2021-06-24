from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from weasyprint import HTML
import tempfile, datetime
from django.views.generic.base import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Company, Employee
from .forms import CompanyForm, EmployeeForm

class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        return context
    
class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = "company/company_update_form.html"
    success_url = "/"

def employeeList(request):
    if request.method =='GET' :
        company_id = int(request.GET.get('companyID'))
        empList = Employee.objects.filter(CompanyInfo__id = company_id)
        return render(request,'employee/list.html' , {'employeess' : empList , 'form' : EmployeeForm()})
    else :
        company = Company.objects.get(id = request.GET['companyID'])
        emp = Employee.objects.create(
            CompanyInfo = company,
            name = request.POST['name']
        )
        return redirect('/employee-list?companyID={}'.format(request.GET['companyID']))

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employee/emp-update.html"
    success_url = ''

    def get_success_url(self):
        return '/employee-list?companyID={}'.format(self.request.GET['companyID'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def export_pdf(request):
    company_id = int(request.GET.get('companyID'))
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachement; filename=EmpList' + \
    str(datetime.datetime.now()) + '.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    empList = Employee.objects.filter(CompanyInfo__id = company_id)
    html_string = render_to_string('employee/pdf-output.html',{'list': empList} )
    html = HTML(string=html_string)
    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()


        output.open(output.name,'rb')
        response.write(output.read())

    return response