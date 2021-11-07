from django.http import HttpResponse
from django.views.generic import View
import threading
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

        stop_container = threading.Thread(target=executeTest.container_handler.stop_container)
        cleanup_files = threading.Thread(target=executeTest.files_handler.cleanup_temp_files)

        stop_container.start()
        cleanup_files.start()


        return HttpResponse(result)