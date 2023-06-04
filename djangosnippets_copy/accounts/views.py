from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

# Create your views here.
from accounts.models import CustomGroup, CustomUser
from accounts.forms import UserForm,InquiryForm,UserCreationForm
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
import csv
import urllib


def top(request):
    users = CustomUser.objects.all()
    print(users)
    context = {"users": users}
    return render(request, "accounts/top.html", context)


def edit(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            obj=form.save()
            obj.save()
            #form.save_m2m()   #ここがキーポイント
            return redirect("accounts_top")
    else:
        form = UserForm(instance=user)
    return render(request, "accounts/user_edit.html", {"form": form})


class Delete(DeleteView):
    model = CustomUser
    template_name = "accounts/delete.html"
    success_url = reverse_lazy("accounts_top")


def inquiry(request):
    if request.method=="POST":
        form=InquiryForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.save()
            print(obj)
            return redirect("accounts_top")

    form=InquiryForm()
    return render(request,"accounts/message.html",{"form":form})

def csv_export(request):
    response = HttpResponse(content_type="text/csv; charset=utf-8")

    f = "user_list" + ".csv"
    filename = urllib.parse.quote((f).encode("utf8"))
    response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(filename)

    writer = csv.writer(response)
    users = CustomUser.objects.all()
    writer.writerow(["id", "username", "origin_group", "origin", "role"])
    for user in users:
        writer.writerow(
            [user.id, user.username, user.origin_group.group_id, user.show_roles()]
        )
    return response



def create_user(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            print(obj)
            obj.save()
            form.save_m2m()
            return redirect("accounts_top")

    form=UserCreationForm()
    return render(request,"accounts/user_create.html",{"form":form})
