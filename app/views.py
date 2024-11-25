from django.shortcuts import render

def login_page (request):
  return render(request, 'app/home.html')
# Create your views here.
