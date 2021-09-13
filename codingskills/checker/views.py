from django.http import HttpResponse
from django.views.generic import View
import json

from .handlers import ExecuteTest

class HandleFrontendData(View):
    def post(self, request, *args, **kwargs):
        payload = request.body
        data = json.loads(payload)

        task_input = data['task_input']
        task_output = data['task_output']
        task_code = data['task_code']
        task_language = data['task_language']
        
        return HttpResponse('ok')


