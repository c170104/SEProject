from django.shortcuts import render
import urllib
import json
from django.http import HttpResponse

# Create your views here.
url = "https://data.gov.sg/api/action/datastore_search?resource_id=0c14ceec-da1b-43c6-92fc-e82d7219840b&limit=5"

def index(request):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    socket = urllib.request.urlopen(req)
    fileObj = json.loads(socket.read())
    socket.close()
    return render(request, 'ChildCares/index.html', {'active_page': 'childcares','content': fileObj['result']['records']})

def filter(request):
    return render(request, 'ChildCares/index.html', {'active_page': 'childcares', 'content': ["FILTERED DATA HERE"]})
