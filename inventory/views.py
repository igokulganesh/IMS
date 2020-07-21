from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import *	
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'inventory/index.html')

def dashboard(request):
	return render(request, 'inventory/dashboard.html')

	
def employee(request):
	Emps = Employee.objects.all()
	return render(request, 'inventory/employee.html', { 'Emps': Emps })    

def add_employee(request):
	if request.method=="POST":
		form=EmployeeForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/employee')
	else:
		form=EmployeeForm()
		return render(request,'inventory/add_employee.html',{'form': form})


def emp_edit(request, emp_id):
	emp = get_object_or_404(Employee, pk=emp_id)
	if request.method == "POST":
		form = EmployeeForm(request.POST, instance=emp)
		if form.is_valid():
			form.save()
			return redirect('/employee')
	else:
		form = EmployeeForm(instance=emp)
		return render(request, 'inventory/edit_emp.html', {'form': form, 'emp' : emp})



def delete_employee(request, emp_id):
	Employee.objects.filter(id=emp_id).delete()
	Emps = Employee.objects.all()
	return render(request, 'inventory/employee.html', { 'Emps' : Emps } )


def customer(request):
	Cust = Customer.objects.all()
	return render(request, 'inventory/customer.html', { 'Cust': Cust })	

def add_customer(request):
	if request.method=="POST":
		form=CustomerForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/customer')
	else:
		form=CustomerForm()
		return render(request,'inventory/add_customer.html',{'form': form})

def cust_edit(request, cus_id):
	emp = get_object_or_404(Customer, pk=cus_id)
	if request.method == "POST":
		form = CustomerForm(request.POST, instance=emp)
		if form.is_valid():
			form.save()
			return redirect('/customer')
	else:
		form = CustomerForm(instance=emp)
		return render(request, 'inventory/edit_cust.html', {'form': form})



def delete_customer(request, cus_id):
	Cust = get_object_or_404(Customer, pk=cus_id)
	if request.method=="POST":
		emp.delete()

	else:
		return render(request, 'inventory/customer.html', { 'Cust' : Cust } )			


def update_work(request, emp_id):
	emp = get_object_or_404(Employee, pk=emp_id)
	wk = Work.objects.filter(emp=emp_id)

	if request.method=="POST":
		form=WorkForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/employee')
	else:
		wform = WorkForm()
		return render(request, 'inventory/update_work.html', {'wform' : wform, 'wk' : wk, 'emp' : emp })

