from django.http import HttpResponse
from django.views.generic import View
from django.core.signals import request_finished

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

        executeTest = ExecuteTest(task_input, task_output, task_code, task_language)
        result = executeTest.run_test()

        # request_finished.connect(executeTest.container_handler.stop_container(), executeTest.files_handler.cleanup_temp_files())
        return HttpResponse(result)

        #Check with multithreading vs django.signals