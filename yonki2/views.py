from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def vista1(request):
 return HttpResponse("<h1>yonki2 - vista1</h1><p>holda desde yonki2/vista1</p>")



def vista2(request):
 return HttpResponse("<h1>yonki2 - vista2</h1><p>holda desde yonki2/vista2</p>")
