from django.shortcuts import render, redirect
import markdown2
from . import util
import random




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

def randomize(request):
            random_page = random.choice(util.list_entries())                    
            return redirect('title', title=random_page)


                    
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
    