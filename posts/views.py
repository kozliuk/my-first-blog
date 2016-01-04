from django.shortcuts import render
from django.shortcuts import redirect
from posts.forms import PostsForm
from django.shortcuts import get_object_or_404
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

from posts.models import Posts


def showPosts(request):
	posts = Posts.objects.all()
	return render(request,"home.html",{"posts":posts})

def about(request):
	return render(request,"about.html",{})

def showPost(request,id):
	post = Posts.objects.get(pk=id)
	context = {
		"post":post
	}
	return render(request,"post.html",context) 

@login_required
def addPost(request,form=None):
	if not request.method == "POST":
		form = PostsForm()
		context = {
			"form":form
		}
		return render(request,"add.html", context)
	else:
		form_to_save = PostsForm(request.POST)
		if form_to_save.is_valid():

			form_to_save.save() 
		return redirect('/blog/')

@login_required
def editPost(request, id):
	post = get_object_or_404(Posts,pk=id)
	if request.method == "POST":
		form = PostsForm(request.POST, instance=post)
		if form.is_valid():
			post.save()
			return redirect('/blog/')
	else:
		form = PostsForm(instance=post)
		context = {
			"form":form
		}
	return render(request, "edit.html", context)
		

def login_me(request):
	if request.method == "POST":
		username = request.POST['user']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
				if user.is_active:
					auth.login(request, user)
		return redirect('/blog/')
	else:
		return render(request, "login.html", {})

@login_required
def logout_me(request):
	logout(request)
	return redirect('/blog/')

@login_required
def deletePost(request,id):
	post = Posts.objects.get(pk=id)
	post.delete()
	return redirect('/blog/')

def contact(request):
	return render(request, "contact.html", {})