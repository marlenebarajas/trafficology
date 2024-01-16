from django.http import HttpResponse

from .models import Freeway


def index(request):
    freeway_list = Freeway.objects.order_by("-id")

    output = "\n".join([f.name for f in freeway_list])
    return HttpResponse(output, content_type="text")

# def freeways(request, id):
#     response =
