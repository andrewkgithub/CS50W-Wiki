from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from . import util
import markdown2
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)  # Retrieve the entry content
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested page was not found."
        })
    
    # Convert the Markdown content to HTML
    content_html = markdown2.markdown(content)
    
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content_html  # Pass the HTML-converted content to the template
    })

def search(request):
    query = request.GET.get("q", "")  # Get the search query from the form
    entries = util.list_entries()

    if util.get_entry(query):  # If an exact match is found, redirect to that entry's page
        return redirect("entry", title=query)

    # Otherwise, find all entries that contain the query as a substring (case-insensitive)
    results = [entry for entry in entries if query.lower() in entry.lower()]

    return render(request, "encyclopedia/search_results.html", {
        "query": query,
        "results": results
    })

class NewPageForm(forms.Form):
    title = forms.CharField(
        label="Page Title",
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'style': 'width: 100%; margin-bottom: 15px;',
        })
    )
    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'style': 'width: 100%; height: 300px; margin-bottom: 15px;',  # Custom width and height
        })
    )

def create(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            # Check if entry with the same title already exists
            if util.get_entry(title):
                return render(request, "encyclopedia/create.html", {
                    "form": form,
                    "error": "An entry with this title already exists."
                })
            
            # Save the new entry
            util.save_entry(title, content)
            return redirect("entry", title=title)
    else:
        form = NewPageForm()

    return render(request, "encyclopedia/create.html", {
        "form": form
    })

class EditPageForm(forms.Form):
    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'style': 'width: 100%; height: 300px; margin-bottom: 15px;',
        })
    )

def edit(request, title):
    content = util.get_entry(title)  # Retrieve the existing content of the entry
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested page was not found."
        })

    if request.method == "POST":
        form = EditPageForm(request.POST)
        if form.is_valid():
            new_content = form.cleaned_data["content"]

            # Save the updated content
            util.save_entry(title, new_content)
            return redirect("entry", title=title)
    else:
        form = EditPageForm(initial={"content": content})  # Pre-fill with existing content

    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "form": form
    })

def random_page(request):
    entries = util.list_entries()  # Get all entries
    if entries:
        selected_entry = random.choice(entries)  # Randomly select one
        return redirect("entry", title=selected_entry)
    else:
        return render(request, "encyclopedia/error.html", {
            "message": "No entries found."
        })