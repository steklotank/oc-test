from django import forms
from django.shortcuts import render, redirect
from django.http import HttpRequest
import random
import markdown2
from . import util

class SearchForm(forms.Form):
    query = forms.CharField()

class CreateForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    source = forms.CharField()

class EditForm(forms.Form):
    title = forms.CharField()
    source = forms.CharField()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), 
        "header" : "All pages"
        })

def title(request, title):
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = util.get_entry(title) 
            source = form.cleaned_data.get("source")
            return render (request,"encyclopedia/editor.html", {
            "header" : "Edit page",
            "title": title, 
            "content": content,
            "source" : 'Title'
            })
        else:
            return render(request,"encyclopedia/title.html",{
                "title": "Error",
                "article" : "Form is not valid"
                })
    else:
        if util.get_entry(title):
            return render (request,"encyclopedia/title.html", {
                "title": title, 
                "article": markdown2.markdown(util.get_entry(title))
                })
        else:
            return render (request,"encyclopedia/404.html",{
            "entries": util.list_entries() 
            })

def editor(request):
        if request.method == "POST":
            form = CreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get("title")
                content = form.cleaned_data.get("content")
                source = form.cleaned_data.get("source")
                if util.get_entry(title) and source == 'Editor':
                        return render(request,"encyclopedia/index.html",{
                        "header" : "Page already exist, if you want to edit page try on of these",
                        "entries": util.list_entries(),
                        })
                else:    
                        util.save_entry(title, content)
                        return redirect('title', title=title)

            else:
                return render(request,"encyclopedia/title.html",{
                "title": "Error",
                "article" : "Form is not valid"
                })
        else:
            return render(request, "encyclopedia/editor.html",{
            "header" : "New page",
            "hide_button" : "submit", 
            "source" : 'Editor'
            })

def random_page(request):   
            random_page = random.choice(util.list_entries()) 
            return redirect('title', title=random_page)

def search(request): 
        if request.method == "POST":
            form = SearchForm(request.POST)
            if form.is_valid():
                query = form.cleaned_data.get("query")
                if util.get_entry(query):
                    return redirect('title', title=query)
                else:  
                    list_to_search = util.list_entries()
                    result = []
                    for item in list_to_search:
                        if query.lower() in item.lower():
                            result+=[item]               
                    return render(request, "encyclopedia/search.html", {
                    "entries" : result,
                     })
            else:
                return render(request,"encyclopedia/title.html",{
                "title": "Error",
                "article" : "Form is not valid"
                })  
