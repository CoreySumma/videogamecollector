from django.shortcuts import render

# Create your views here.
# Define the home view
# **REMINDER** Include an .html file extension
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')