# urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from rest_framework.routers import DefaultRouter
from inventory import views

router = DefaultRouter()
router.register("", views.ProductViewSet)

def hello_name(request):
    """
    A simple view that returns 'Hello, {name}' in JSON format.
    Uses a query parameter named 'name'.
    """
    # Get 'name' from the query string, default to 'World' if missing
    name = request.GET.get("name", "World")
    return JsonResponse({"message": f"Hello, {name}!"})

def hello_world(request):
    return HttpResponse("Testing by Vardhan.")
    # return HttpResponse("Hello, world! This is our interneers-lab Django server.")

def redirect_to_home(request):
    return redirect("/home")

def show_home(request):
    return render(None, "home.html")

def show_products(request):
    return render(request, "show_prods.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("hello/", hello_world),
    path("hello/", hello_name),
    # Example usage: /hello/?name=Bob
    # returns {"message": "Hello, Bob!"}
    # path("", include(router.urls)),
    # path("", redirect_to_home),
    path("home/", show_home),
    # path("show_products/", show_products),
    path("show_products/", include(router.urls)),
]
