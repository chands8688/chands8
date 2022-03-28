from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':'56','b':'69'}
    return render(request,'ifelse.html',d)