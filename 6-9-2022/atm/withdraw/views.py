from django.shortcuts import render

# Create your views here.
def withdraw1_details(request):
    location="hyderabad"
    name="sbi"
    type="cdm"
    capacity=10000
    w1_details={"lo":location,"na":name,"ty":type,"ca":capacity}
    return render(request,"wamount1.html",w1_details)

def withdraw2_details(request):
    location="hyderabad"
    name="sbi"
    type="cdm"
    capacity=10000
    w2_details={"lo":location,"na":name,"ty":type,"ca":capacity}
    return render(request,"wamount2.html",w2_details)

def withdraw3_details(request):
    location="hyderabad"
    name="sbi"
    type="cdm"
    capacity=10000
    w3_details={"lo":location,"na":name,"ty":type,"ca":capacity}
    return render(request,"wamount3.html",w3_details)