from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
	if request.method == 'POST':
		form=ListForm(request.POST )

		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messages.success(request,("item has been added to the list !!"))
			return render(request, 'home.html',{'all_items':all_items})
	else:	
		all_items = List.objects.all
		return render(request, 'home.html',{'all_items':all_items})

def about(request):
	context = {'first':'Pranav','last': 'Bhandari'}
	return render (request,'about.html',context)
# Create your views here.

def delete(request,list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request,("item has been Deleted!!"))
	return redirect('home')

def cross_off(request,list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('home')

def uncross(request,list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('home')

def edit(request,list_id):
	if request.method == 'POST':
		item = List.objects.get(pk=list_id)

		form=ListForm(request.POST,instance=item)

		if form.is_valid():
			form.save()
			messages.success(request,("item has been Edited !!"))
			return redirect('home')
	else:	
		item = List.objects.get(pk=list_id)
		return render(request, 'edit.html',{'item':item})