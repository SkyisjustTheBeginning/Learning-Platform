from django.shortcuts import render

def sci_homepage(request):
    return render(request,'sci_homepage.html',{'name':'Gabriel'})
def bio(request):
    return render(request,'biology.html')
def chem(request):
    return render(request,'chemistry.html')
def phy(request):
    return render(request,'physics.html')
