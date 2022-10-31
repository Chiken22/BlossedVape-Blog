from cgitb import html
from multiprocessing import context
from django.shortcuts import render
from my_vape.models import Vape
# Create your views here.
def vapes(request):
    vapes = Vape.objects.all()

    context_dict = {"vapes": vapes}

    return render(
        request=request,
        context=context_dict,
        template_name="my_vape/vape_list.html",
    )
