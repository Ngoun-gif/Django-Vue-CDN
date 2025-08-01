from django.shortcuts import render

# Create your views here.


# Frontend Views
def frontend_home(request):
    context = {
        'active_page': 'home'
    }
    return render(request, 'frontend/home/index.html', context)

def frontend_about(request):
    context = {
        'active_page': 'about'
    }
    return render(request, 'frontend/about/index.html', context)

def frontend_service(request):
    context = {
        'active_page': 'services'  # match the key you check in template
    }
    return render(request, 'frontend/service/index.html', context)

def frontend_technician(request):   # fixed function name
    context = {
        'active_page': 'technician'
    }
    return render(request, 'frontend/technician/index.html', context)  # fix folder name to 'technician'

def frontend_contact(request):
    context = {
        'active_page': 'contact'
    }
    return render(request, 'frontend/contact/index.html', context)

def frontend_booking(request):
    context = {
        'active_page': 'booking'  # optional if you want to highlight booking in nav
    }
    return render(request, 'frontend/booking/index.html', context)