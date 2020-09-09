from django.shortcuts import render
import markdown2
from . import util




def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries() 
    })

def title(request, title):
	return render (request,"encyclopedia/title.html", {
		"title": title, 
        "article": markdown2.markdown(util.get_entry(title))
	})

def editor(request, title):
	return render (request,"encyclopedia/title.html", {
		"title": title, 
        "article": util.get_entry(title)
	})