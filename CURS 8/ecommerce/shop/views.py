from django.shortcuts import render
from .models import Product

# Create your views here.

def product_list_view(request):
	context = {}
	return render(request, 'product_list.html', context)

def product_details_view(request, slug):
	current_product_model = Product.objects.filter(slug = slug)[0]
	context = {
		"current_product_model" : current_product_model
	}
	return render(request, 'product_details.html', context)
