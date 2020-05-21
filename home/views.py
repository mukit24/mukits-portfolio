from django.shortcuts import render

# Create your views here.
def home_content(request):
    return render(request, "home_content.html")
