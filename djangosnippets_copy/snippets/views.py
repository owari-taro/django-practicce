from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from .models import Snippet

from django.contrib.auth.decorators import login_required

# Create your views here.
from snippets.forms import SnippetForm


def top(request):
    snippet = Snippet.objects.all()
    context = {"snippets": snippet}
    return render(request, "snippets/top.html", context)


def snippet_edit(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    if snippet.created_by != request.user.id:
        return HttpResponseForbidden("not allowed")
    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect("snippet_detail", snippet_id=snippet_id)
    else:
        form = SnippetForm(instance=snippet)
    return render(request, "snippets/snippet_edit.html", {"form": form})


def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render(request, "snippets/snippet_detail.html", {"snippet": snippet})


@login_required
def snippet_new(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            return redirect("snippet_detail", snippet_id=snippet.pk)
    else:
        form = SnippetForm
    return render(request, "snippets/snippet_new.html", {"form": form})
