from django.shortcuts import render


def home(request):
    context = {
        'home_link_selected': 'active',
    }
    return render(request, 'home.html', context)


def contact(request):
    context = {
        'contact_link_selected': 'active',
    }
    return render(request, 'contact.html', context)