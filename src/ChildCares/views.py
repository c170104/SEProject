from django.shortcuts import render, redirect
from . import apidata

import sys

# Create your views here.
<<<<<<< HEAD
=======
url = "https://data.gov.sg/api/action/datastore_search?resource_id=0c14ceec-da1b-43c6-92fc-e82d7219840b"
>>>>>>> origin/master

def index(request):
    # data API
    query = request.GET.get('q', '')
    results = apidata.main(query)

    # pagination
    pageNumber = request.GET.get('p', '1')
    if(pageNumber.isdigit()):
        itemStart = (int(pageNumber)-1) * 20
        itemEnd = itemStart + 20
    else:
        itemStart = 0
        itemEnd = 20
    pages = int(len(results) / 20)
    results = results[itemStart:itemEnd]
    
    return render(request, 'ChildCares/index.html', {'active_page': 'childcares','content': results, 'page_number': int(pageNumber), 'pages': range(pages)})
<<<<<<< HEAD
=======

def filter(request):
    return render(request, 'ChildCares/index.html', {'active_page': 'childcares', 'content': ["FILTERED DATA HERE"]})
>>>>>>> origin/master

def moreinfo(request):
    #
    getCentreCode = request.GET.get('cc', '')
    results = apidata.main(getCentreCode)
    if(getCentreCode != ''):   
        # print(results)
        return render(request, 'ChildCares/moreinfo.html', {'content': results})
    return redirect('/')
    
