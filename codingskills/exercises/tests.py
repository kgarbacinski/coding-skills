from django.test import TestCase, Client

'''
Test views
'''

class TestHomeView(TestCase):
    HOME_URL = '/'

    def setUp(self):
        self.client = Client()

    def test_should_return_200_when_app_is_running(self) -> None:
        response = self.client.get(TestHomeView.HOME_URL)

        self.assertEqual(response.status_code, 200)

class TestExercisesDetailView(TestCase):
    HOME_URL = '/palindrome'

    def setUp(self):
        self.client = Client()

    def test_should_return_200_when_palindrome_window_is_rendered(self) -> None:
        response = self.client.get(TestHomeView.HOME_URL)

        self.assertEqual(response.status_code, 200)

'''
Test models
'''
from exercises.models import Tasks, Tests

class TestTasksModel(TestCase):
    
    def __init__(self):
        self.generateTestData()

    def generateTestData(self) -> None:
        record = Tasks(task_id = 999, task_name = 'Test task', task_content = 'Test task content')
        record.save()
 

    def setUp(self) -> None:
        self.test_task = Tasks.objects.get(task_id = 999)

    def test_get_task_id(self) -> None:
        self.assertEqual(self.test_task.task_id, 999, msg="Task should equal: 999")

    def test_task_title_content(self) -> None:
        expected_task_name = "Test Task"

        self.assertEqual(
            self.test_task.task_name, expected_task_name, msg="Title should be 'Test task'"
        )

    def test_task_content(self) -> None:
        expected_task_content = 'Test task content'

        self.assertEqual(
            self.test_task.task_name, expected_task_content, msg="Content should be 'Test task content'"
        )
