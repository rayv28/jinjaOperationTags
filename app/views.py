from django.shortcuts import render

# Create your views here.
def fun(request):
  dict={'a':100}
  return render(request,'rev.html',dict)