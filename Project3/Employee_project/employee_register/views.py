from django.shortcuts import render,redirect,HttpResponse
from .forms import EmployeeForms
from .models import Employee
# Create your views here.
def home(request):
    return render(request,"employee_register/base.html")
def employee_list(request):
    
    context={'employee_list':Employee.objects.all()}    
    return render(request,"employee_register/employee_list.html",context)
def employee_form(request,id=0):
    if request.method=="GET":
        if id==0:
            form=EmployeeForms()
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForms(instance=employee)
        return render(request,"employee_register/employee_form.html",{'forms':form})
    else:
        if id==0:
            form=EmployeeForms(request.POST)
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForms(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list/')



    
def employee_delete(request,id):
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list/')