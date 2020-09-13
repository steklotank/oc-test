query="ml"
list_to_search = ["Python", "CSS", "HTML", "Django" ]
result = []
for item in list_to_search:
    if query.lower() in item.lower():
        result+=[item]
        print(result)
        break     
    else:
        print('No match')
                  
                         