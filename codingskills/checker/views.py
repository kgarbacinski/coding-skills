from django.http import HttpResponse
from django.views.generic import View
import json

from .execute_test import ExecuteTest

class HandleFrontendData(View):
    def post(self, request, *args, **kwargs):
        payload = request.body
        data = json.loads(payload)

        task_input = str(data['task_input'])
        task_output = str(data['task_output'])
        task_code = str(data['task_code'])
        task_language = str(data['task_language']).lower()

        test_result = ExecuteTest(task_input, task_output, task_code, task_language).run_test()
        
        return HttpResponse(test_result)