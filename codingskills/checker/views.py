from django.http import HttpResponse, HttpRequest
from django.http import JsonResponse
from django.views.generic import View


class GetExercise(View):
    def post(self, HttpRequest, *args, **kwargs):
        data = HttpRequest()
        print(data)
        return HttpResponse('Ok!')