from django import forms
from django.shortcuts import render, redirect
import markdown2
from . import util
import random
from django.http import HttpRequest
import re


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
                query = form.cleaned_data.get("query")

                if util.get_entry(query):
                    return redirect('title', title=query)

                else:  

                    list_to_search = util.list_entries()
                    prase_to_search = f"r'{query}'"
                    result = []
                    for item in list_to_search:
                        if query.lower() in item.lower() :
                            result+=[item]               
                    return render(request, "encyclopedia/search.html", {
                        "entries" : result,
                         })
                        
                        
                         
                   
                     

        

                    
"""
def editor(request, title):
	return render (request,"encyclopedia/title.html", {
		"title": title, 
        "article": util.get_entry(title)
	})
"""
    