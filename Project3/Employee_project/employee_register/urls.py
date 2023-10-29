from django.urls import path,include
from . import views

urlpatterns=[
  path('',views.home,name="home"),
  path('list/',views.employee_list,name="employee_list"), # get and post request for display all the information 
  path('<int:id>/',views.employee_form,name='employee_update'), # get and post request for update the operation 
  path('form/',views.employee_form,name='employee_insert'),# get and post request to insert in the database
  path('delete/<int:id>/',views.employee_delete,name="employee_delete"), #get and post request for deletion in the database
  
 ] 