from django import forms
from .models import *
from django.shortcuts import render

class UpImgForm(forms.ModelForm):
    class Meta:
        model = UpImg
        fields = ['name', 'up_img']

def form_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.method == 'POST':
            form = CustomForm(request.POST)
            if form.is_valid():
                if form.cleaned_data.get('key') == EncKey.objects.last().my_key:
                    return view_func(request, *args, **kwargs)
                else:
                    form.add_error('key', 'Invalid value')
        else:
            form = CustomForm()
        return render(request, 'mainapp/form.html', {'form': form})
    return wrapper

class CustomForm(forms.Form):
    key = forms.CharField(max_length=6)