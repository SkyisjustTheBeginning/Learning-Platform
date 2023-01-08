from django.shortcuts import render

# Create your views here.
def algebra(request):
    return render(request,'algebra.html')
def geometry(request):
    return render(request,'geometry.html')