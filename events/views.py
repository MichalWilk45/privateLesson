from django.shortcuts import render

def home(request):
    name = "Michał"
    return render(request, 'home.html', {
        "name": name
    })
