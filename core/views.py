from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello From Abo 6!</h1>')

def contact(request):
	context = {
	'title' : 'Contact Us'
	}
	return render(request, 'contact.html', context)

def about(request):
	context = {
	'title' : 'About Us'
	}
	return render(request, 'about.html', context)

def blog(request):
	context = {
	'title' : 'Blog'
	}
	return render(request, 'index.html', context)

def post(request):
	context = {
	'title' : 'Post'
	}
	return render(request, 'post.html', context)
