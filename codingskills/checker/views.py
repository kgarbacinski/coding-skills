import threading
import json

from django.http import JsonResponse
from django.views.generic import View
from django.http.request import QueryDict


from .execute_test import ExecuteTest


class HandleFrontendData(View):
    """
    This is the endpoint for frontend to get data and call ExecuteTest to initiate the sequence of code validation.
    Threading implemented to cleanup generated file from FilesHandler and stop container run by ContainerHandler.
    Class returns jsonified response from backend to frontend. Sample response: {'result': 'passed'}

    Caller: None
    """

    def post(self, request: QueryDict, *args, **kwargs) -> str:
        payload = request.body
        data = json.loads(payload)

        task_input = str(data["task_input"])
        task_output = str(data["task_output"])
        task_code = str(data["task_code"])
        task_language = str(data["task_language"]).lower()

        executeTest = ExecuteTest(task_input, task_output, task_code, task_language)
        test_result = executeTest.run_test()
        data = {"response": test_result}

        stop_container = threading.Thread(
            target=executeTest.container_handler.stop_container
        )
        cleanup_files = threading.Thread(
            target=executeTest.files_handler.cleanup_temp_files
        )

        stop_container.start()
        cleanup_files.start()

        return JsonResponse(data)
