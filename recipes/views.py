from django.http import JsonResponse


def index(request):
    if request.method == "GET":
        return JsonResponse({"name": "kelvin"})
