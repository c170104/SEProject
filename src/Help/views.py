from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Help/index.html', {'active_page': 'help'})