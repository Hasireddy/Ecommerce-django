from django.shortcuts import render, get_object_or_404
from django.http import Http404,HttpResponse
from .models import Product, Category

# Create your views here.

def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    available_products = Product.objects.filter(available=True)

    if category_slug is not None:
        """
        category = Category.objects.filter(slug=category_slug)
        if len(category) == 0:
            return Http404(f"No category found with slug: {category_slug}")
        """
        category = get_object_or_404(Category, slug=category_slug)
        available_products = available_products.filter(category=category)
        return render(request, "shop/product/list.html", {"products": available_products})


def product_details(request,id):
    # product = Product.objects.get(id=id)
    product = get_object_or_404(Product, id)
    return render(request,"product-details.html",{'data':product})

def home(request):
    return render(request,"home.html")