from django.shortcuts import render

# Create your views here.
def menu_details(request):
    a="menu"
    b="food items"
    c="MENU"
    item="Biryani"
    price="user-friendly"
    chocolates="dairymilk"
    reviews="bhagavaan"
    greetings="thanks for choosing our hotel"
    list=[1,2,3,4,5,6,7,8]
    d={'a':a,'b':b,'c':c,'ite':item,'pr':price,'choco':chocolates,'rev':reviews,'li':list,'gr':greetings}
    return render(request,"1.html",context=d)

