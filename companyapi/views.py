from django.http import HttpResponse

def home_page(Request):
    print("Home page requested")
    return HttpResponse("<h1>This is Home Page<h1>")
