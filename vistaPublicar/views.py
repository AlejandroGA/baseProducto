from django.shortcuts import render, redirect, render_to_response

# Create your views here.

def base(request):
    return render(request,'base.html')