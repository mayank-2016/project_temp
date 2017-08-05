from django.shortcuts import render

def view(response):
    return render(response, 'ShelfLife/index.html')