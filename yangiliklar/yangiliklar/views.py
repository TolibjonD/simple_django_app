from django.shortcuts import render, redirect
from postlar.models import Postlar
from postlar.forms import PostsForm

def home_page(request):
    post_form = PostsForm()
    if request.method == "POST":
        post_form = PostsForm(data=request.POST, files=request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect("home")
    postlar = Postlar.objects.all().order_by("-created_at")
    return render(request , "home_page.html", {"form": post_form, "posts": postlar})

def about_page(request):
    return render(request , "about.html")