from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'Helloshop',
        'subtitle':'Learning Django Framework'
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'title':'About',
        'subtitle':'There is one impostor Among Us'
    }
    return render(request, 'about.html', context)

def testimonial(request):
    context = {
        'title':'Testmonial',
    }
    return render(request, 'testmonial.html', context)

def clients(request):
    context = {
        'title':'Shop',
    }
    return render(request, 'clients.html', context)

def contact(request):
    context = {
        'title':'Contact',
    }
    return render(request, 'contact.html', context)