from django.shortcuts import render
from .models import Products, Categories


def filter_products(request, category_category_slug):
    context = Categories.objects.get(slug=category_category_slug)
    context2 = Products.objects.filter(category_id=context.id)
    # category_category_slug = context.slug
    return render(request, 'products/product_detail.html', {'context': context, 'context2': context2})

