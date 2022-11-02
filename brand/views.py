
# Create your views here.
from cgitb import html
from multiprocessing import context
from django.shortcuts import render
from brand.models import Brand 
def brands(request):
    brands = Brand.objects.all()

    context_dict = {"brands": brands}

    return render(
        request=request,
        context=context_dict,
        template_name="brand/brand_list.html",
    )
