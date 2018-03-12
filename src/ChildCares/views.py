from django.shortcuts import render, redirect
from . import apidata

import sys

# Create your views here.
globaldata = None

def index(request):
    # data API
    query = request.GET.get('q', '')
    results = apidata.main(query)
    globaldata = results

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

def moreinfo(request):
    #
    getPage = request.GET.get('p', '')
    getDataId = request.GET.get('i', '')
    print(globaldata)
    if(getPage != '' and getDataId != ''):   
        return render(request, 'ChildCares/moreinfo.html', {'content': globaldata[getPage*20+getDataId]})
    return redirect('/')
    
