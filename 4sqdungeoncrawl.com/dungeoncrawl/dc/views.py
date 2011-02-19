from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")

def foursquare_callback(request):
    """Endpoint for foursquare API calls"""
    return HttpResponse("FIXME, NOT YET IMPLEMENTED")
