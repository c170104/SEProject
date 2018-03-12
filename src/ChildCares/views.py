from django.shortcuts import render
import urllib
import json
import sys

# Create your views here.
url = "https://data.gov.sg/api/action/datastore_search?resource_id=0c14ceec-da1b-43c6-92fc-e82d7219840b"

def index(request):
    # data API
    query = request.GET.get('q', '')
    new_URL = url + "&q=" + query
    req = urllib.request.Request(new_URL, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        fileObj = json.loads(response.read().decode('utf-8'))
        response.close()
    results = fileObj['result']['records']

    # pagination
    pageNumber = request.GET.get('p', '1')
    if(pageNumber.isdigit()):
        itemStart = (int(pageNumber)-1) * 20
        itemEnd = itemStart + 20
    else:
        itemStart = 0
        itemEnd = 20
<<<<<<< HEAD
    pages = int(len(results) / 20)
    results = results[itemStart:itemEnd]
    
    return render(request, 'ChildCares/index.html', {'active_page': 'childcares','content': results, 'page_number': int(pageNumber), 'pages': range(pages)})
=======

    results = results[itemStart:itemEnd]
    
    return render(request, 'ChildCares/index.html', {'active_page': 'childcares','content': results})
>>>>>>> 0142a0338a25e237b7feca0327c6c43d3dcd8e2a

def filter(request):
    return render(request, 'ChildCares/index.html', {'active_page': 'childcares', 'content': ["FILTERED DATA HERE"]})

    
