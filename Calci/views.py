from django.shortcuts import render

# Create your views here.
def calc(req):
    return render(req,'calculator.html')