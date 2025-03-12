"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, re_path, include
from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# API root view with HATEOAS links
@api_view(['GET'])
def api_root(request):
    """
    API root view that provides information about available endpoints.
    """
    base_url = request.build_absolute_uri('/').rstrip('/')
    
    api_info = {
        "message": "Welcome to the Bookstore API",
        "version": "1.0.0",
        "documentation": "This API provides endpoints for managing a bookstore inventory and orders",
        "endpoints": {
            "products": {
                "url": f"{base_url}/bookstore/v1/product/",
                "methods": ["GET", "POST"],
                "description": "List all products or create a new product"
            },
            "categories": {
                "url": f"{base_url}/bookstore/v1/category/",
                "methods": ["GET", "POST"],
                "description": "List all categories or create a new category"
            },
            "orders": {
                "url": f"{base_url}/bookstore/v1/order/",
                "methods": ["GET", "POST"],
                "description": "List all orders or create a new order"
            },
            "admin": {
                "url": f"{base_url}/admin/",
                "description": "Admin interface (requires admin credentials)"
            },
            "authentication": {
                "url": f"{base_url}/api-token-auth/",
                "method": "POST",
                "description": "Obtain authentication token by posting username and password"
            }
        },
        "usage_example": {
            "authentication": "POST /api-token-auth/ with {'username': 'your_username', 'password': 'your_password'}",
            "using_token": "Include header 'Authorization: Token your_token_value' in subsequent requests"
        }
    }
    return Response(api_info)

urlpatterns = [
    # Root URL handler
    path("", api_root, name="api_root"),
    
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    re_path("bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("bookstore/(?P<version>(v1|v2))/", include("product.urls")),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
