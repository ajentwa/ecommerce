from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request,'pages/home.html')

def about(request):
    return render(request,'pages/about.html')

@login_required
def userProfile(request):
    user = request.user
    context = {'user':user}
    return render(request,'pages/profile.html',context)



    