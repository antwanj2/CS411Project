from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'prototype/post_list.html', {})
    #i changed this to say prototype instead of blog because my template is looking for blog not prototype
    