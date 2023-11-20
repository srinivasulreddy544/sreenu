from django.shortcuts import render

# Create your views here.
def sri(request):
  d={'a':10}
  return render(request,'sri.html',d)
def sreenu(request):
  c={'a':100,'b':20}
  return render(request,'sreenu.html',c)
def reddy(request):
  e={'a':100,'b':20,'c':2}
  return render(request,'reddy.html',e)
