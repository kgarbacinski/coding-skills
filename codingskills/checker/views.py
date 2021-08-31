from django.http import HttpResponse
from django.views.generic import View
import json


class HandleFrontendData(View):
    def post(self, request, *args, **kwargs):
        payload = request.body
        data = json.loads(payload)

        task_code = data['task_code']
        task_input = data['task_input']
        task_output = data['task_output']
        
        return HttpResponse(PerformTest(task_code, task_input, task_output).result())


class PerformTest:
    def __init__(self, code, input, output):
        self.code = code
        self.input = input
        self.output = output

    def result(self):
        return f'OK!: {self.code}, {self.input}, {self.output}'