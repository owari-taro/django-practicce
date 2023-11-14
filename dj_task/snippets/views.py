from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from .models import Snippet,Task
from django.contrib.auth.decorators import login_required
import time
from .forms import UploadForm,SearchForm
from django.core.files.uploadedfile import UploadedFile
# Create your views here.
from snippets.forms import UploadForm,FeedBackForm,TaskSearchForm
from logging import getLogger
#from .upload import save_file
from django.core.files.storage import FileSystemStorage
from django import forms



logger=getLogger(__name__)
def top(request):
    tasks = Task.objects.all()
    print(tasks)
    context = {"tasks": tasks,"form":TaskSearchForm()}
    return render(request, "snippets/top.html", context)


def snippet_edit(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    if snippet.created_by != request.user.id:
        return HttpResponseForbidden("not allowed")
    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
        #redirect("snippet_detail", snippet_id=snippet_id)
    else:
        form = SnippetForm(instance=snippet)
    return render(request, "snippets/snippet_edit.html", {"form": form})

def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render(request, "snippets/snippet_detail.html", {"snippet": snippet})

#@login_required
def upload(request):
    if request.method == "POST":
        logger.info("post")
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            task=Task.objects.create()
            logger.info(f"new {task.id=} is created")
            old_f,new_f=form.files["old_file"],form.files["new_file"]
            print(type(old_f))
            print(old_f.size)
            FileSystemStorage(location=f"/tmp/{task.id}").save(old_f.name, old_f)
            FileSystemStorage(location=f"/tmp/{task.id}").save(new_f.name,new_f)
            task.old_product,task.new_product=old_f.name,new_f.name
            task.save()
            return render(request,"snippets/upload_complete.html",{"task":task})
        else:
            logger.info("invalid file was loaded")
            return render(request, "snippets/upload.html", {"form": form})
                
    else:
        form = UploadForm
        return render(request, "snippets/upload.html", {"form": form})


def upload_feedback(request):

    if request.method == "POST":
        logger.info("post")
        form = FeedBackForm(request.POST, request.FILES)
        if form.is_valid():
            task=Task.objects.create()
            logger.info(f"new {task.id=} is created")
            old_f,new_f=form.files["old_file"],form.files["new_file"]
            FileSystemStorage(location=f"/tmp/{task.id}").save(old_f.name, old_f)
            FileSystemStorage(location=f"/tmp/{task.id}").save(new_f.name,new_f)
            task.old_product,task.new_product=old_f.name,new_f.name
            task.save()
            return render(request,"snippets/upload_complete.html",{"task":task})
        else:
            logger.info("invalid file was loaded")
            return render(request, "snippets/upload.html", {"form": form})
                
    else:
        form = FeedBackForm
        return render(request, "snippets/feedback.html", {"form": form})


def search(request):
    form=SearchForm
    return render(request,"snippets/search.html",{"form":form})



