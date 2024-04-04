from django.shortcuts import render

def send_fe(request):
    d={'name':'Krishna','age':15}
    return render(request,'template.html',context={'name':'Krishna','age':15})
# Create your views here.
