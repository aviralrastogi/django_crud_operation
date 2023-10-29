from django import forms
from .models import Employee
class EmployeeForms(forms.ModelForm):
    class Meta:
        model=Employee
        fields=('full_name','emp_code','mobile','position')
        labels={
            "full_name":"full_name",
            "emp_code":"emp_code",
            "mobile":"mobile",
            "position":"position",

        }
    def __init__(self,*args,**kwargs):
        super(EmployeeForms,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label="Select"
        self.fields['emp_code'].required=True


