from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def crossdomain(request):
    return render(request, 'crossdomain/crossdomain.xml',{})

def index(request):
    if request.user.is_authenticated():
	return HttpResponse(request.user.username)
    else:
	return HttpResponse('guest')
