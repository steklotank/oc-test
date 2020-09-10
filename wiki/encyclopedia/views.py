from django import forms
from django.shortcuts import render, redirect
import markdown2
from . import util
import random
from django.http import HttpRequest


class NewSearchForm(forms.Form):
    query = forms.CharField()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries() 
    })

def title(request, title):
    if util.get_entry(title):
        return render (request,"encyclopedia/title.html", {
            "title": title, 
            "article": markdown2.markdown(util.get_entry(title))
})
    else:
        return render (request,"encyclopedia/404.html",{
        "entries": util.list_entries() 
    })

def create(request):
    return render(request, "encyclopedia/create.html", {
        
        "entries": util.list_entries() 
    })

def random_page(request):
            random_page = random.choice(util.list_entries()) 
            return redirect('title', title=random_page)

def search(request): 
        if request.method == "POST":
            form = NewSearchForm(request.POST)
            if form.is_valid():
                query= form.cleaned_data.get("query")
                if util.get_entry(query):
                    return redirect('title', title=query)
                else:
                    return render(request, "encyclopedia/search.html", {
                    
                    "query": query 
                    })
        

                    
"""
def editor(request, title):
	return render (request,"encyclopedia/title.html", {
		"title": title, 
        "article": util.get_entry(title)
	})
"""

"""
def search(request):
        return render (request,"encyclopedia/title.html", {
            "title": random.choice(list_entries()), 
            "article": markdown2.markdown(util.get_entry(title))
            })
 """   
    