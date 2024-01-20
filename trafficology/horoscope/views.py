from django.http import HttpResponse
from django.shortcuts import render
from .models import Freeway
from django.views import generic


def index(request):
    return render(request, "index.html")


def daily(request):
    freeway_list = Freeway.objects.order_by("-id")

    output = "\n".join([f.name for f in freeway_list])
    return HttpResponse(output, content_type="text")


def freeways(request):
    freeway_names = Freeway.objects.all()

    context = {
        "freeway_names": freeway_names,
    }
    return render(request, "freeways/index.html", context=context)


# class FreewayListView(generic.ListView):
#     model = Freeway
#     context_object_name = 'freeway_names'
#     template_name = 'freeways/index.html'
