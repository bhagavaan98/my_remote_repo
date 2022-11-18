from django.shortcuts import render

# Create your views here.
def deposit1_details(request):
    print("This is deposite function")
    location="hyderabad"
    name="sbi"
    type="cdm"
    capacity=10000
    d1_details={"lo":location,"na":name,"ty":type,"ca":capacity}
    return render(request,"damount1.html",d1_details)

def deposit2_details(request):
    location="hyderabad"
    name="sbi"
    type="cdm"
    capacity=10000
    d2_details={"lo":location,"na":name,"ty":type,"ca":capacity}
    return render(request,"damount2.html",d2_details)

def deposit3_details(request):
    location="hyderabad"
    name="sbi"
    type="cdm"
    capacity=10000
    d3_details={"lo":location,"na":name,"ty":type,"ca":capacity}
    return render(request,"damount3.html",d3_details)  