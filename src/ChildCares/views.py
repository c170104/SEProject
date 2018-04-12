from django.shortcuts import render, redirect
from ChildCares.controller import ChildCareController
import sys
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    query = request.GET.get('q', '')
    sort = request.GET.get('s', '')
    pageNumber = request.GET.get('p', '1')

    ccCtrler = ChildCareController()

    if(query != ''):
        results = ccCtrler.search(query)
    else:
        results = ccCtrler.get()
    print(results)
    pagination = Paginator(results, 20)
    content = pagination.page(int(pageNumber)).object_list
    maxPageNumber = pagination.num_pages
    if(maxPageNumber == 0):
        pages = range(0)
    elif(int(pageNumber) < 3):
        pages = range(1, int(pageNumber) + 3)
    elif((maxPageNumber - int(pageNumber)) <= 0):
        pages = range(int(pageNumber) - 2, maxPageNumber)
    else:
        pages = range(int(pageNumber) - 2, int(pageNumber) + 3)

    return render(request, 'ChildCares/index.html', {'active_page' : 'childcares', 'content' : content, 'page_number': int(pageNumber), 'pages': pages, 'query' : query, 'sort' : sort})

    
    # # data API
    # 
    # results = apidata.main(urllib.parse.quote_plus(query), sort)

    # # pagination
    # 
    # if(pageNumber.isdigit()):
    #     itemStart = (int(pageNumber)-1) * 20
    #     itemEnd = itemStart + 20
    # else:
    #     itemStart = 0
    #     itemEnd = 20
    # maxPageNumber= int(len(results) / 20)
    # minPageNumber = 1

    # if(maxPageNumber == 0):
    #     pages = range(0)
    # elif(int(pageNumber) < 3):
    #     pages = range(minPageNumber, int(pageNumber) + 3)
    # elif((maxPageNumber - int(pageNumber)) <= 0):
    #     pages = range(int(pageNumber) - 2, maxPageNumber)
    # else:
    #     pages = range(int(pageNumber) - 2, int(pageNumber) + 3)
    # results = results[itemStart:itemEnd]
    
    # return render(request, 'ChildCares/index.html', {'active_page': 'childcares','content': results, 'page_number': int(pageNumber), 'pages': pages, 'query': query, 'sort': sort})

def moreinfo(request):
    #
    # getCentreCode = request.GET.get('cc', '')
    # results = apidata.main(getCentreCode, '')
    # if(getCentreCode != ''):   
    #     # print(results)
    #     return render(request, 'ChildCares/moreinfo.html', {'content': results})
    # return redirect('/')
    return
    
