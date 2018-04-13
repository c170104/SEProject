from django.shortcuts import render, redirect
from ChildCares.controller import ChildCareController
import sys
from django.core.paginator import Paginator, InvalidPage

# Create your views here.

def index(request):
    ccCtrler = ChildCareController()

    query = request.GET.get('q', '')
    sort = request.GET.get('s', '')
    pageNumber = request.GET.get('p', '1')
    
    if(query != ''):
            results = ccCtrler.search(query, sort)
    else:
        results = ccCtrler.get(sort)

    pagination = Paginator(results, 20)

    try: 
        content = pagination.page(int(pageNumber)).object_list
        maxPageNumber = pagination.num_pages
        if(maxPageNumber == 0):
            pages = range(0)
        elif((maxPageNumber - int(pageNumber)) <= 0):
            pages = range(int(pageNumber), maxPageNumber+1)
        else:
            pages = range(int(pageNumber) - 2, int(pageNumber) + 3)
    except InvalidPage:
        content = pagination.page(1).object_list
        error = "Invalid Page number."
        return render(request, 'ChildCares/index.html', {'active_page' : 'childcares', 'content': content, 'error': error})

    return render(request, 'ChildCares/index.html', {'active_page' : 'childcares', 'content' : content, 'page_number': int(pageNumber), 'pages': pages, 'query' : query, 'sort' : sort})

def moreinfo(request):
    success = ''
    error = ''
    ccCtrler = ChildCareController()

    getCentreCode = request.GET.get('cc', '')
    childCare = ccCtrler.search(getCentreCode, '', searchType="cc")

    if request.method == 'POST':
        if not ccCtrler.createReview(request.POST):
            error = "Review failed, Please try again."
        else:
            success = "Review successfully added."

    if(getCentreCode != ''):   
        # print(results)
        return render(request, 'ChildCares/moreinfo.html', {'content': childCare, 'success': success, 'error': error,})
    return redirect('/')
    
