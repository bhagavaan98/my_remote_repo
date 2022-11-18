from django.shortcuts import render

# Create your views here.
import datetime
def date_details(request):
    today={'name':'bhagavaan','t':datetime.datetime.now()}
    return render(request, 'home.html',context=today)