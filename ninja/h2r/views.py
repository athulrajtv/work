from django.shortcuts import render

# Create your views here.
def hellofunction(request):
    return render(request,"book.html")