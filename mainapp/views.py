from django.shortcuts import render, redirect
from .forms import *
from django.urls import reverse
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required

@form_required
def home(request):
    context = {
        'my_images': UpImg.objects.all().order_by('-pk'),
        'my_key': EncKey.objects.last(),
    }
    return render(request, 'mainapp/home.html', context)



def up_img_view(request):
    if request.method == 'POST':
        form = UpImgForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Your image has been uploaded successfully !')
            return redirect('home')
    else:
        form = UpImgForm()
    return render(request, 'mainapp/index.html', {'form':form})