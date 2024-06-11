from django.shortcuts import render

def home(request):
    '''
        Displaying homepage
    '''
    return render(request, 'arrows/home.html')
