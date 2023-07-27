from django.shortcuts import render

# Create your views here.
def edu(request):
    context={'skills':'active'}
    return render(request,'skills.html',context)