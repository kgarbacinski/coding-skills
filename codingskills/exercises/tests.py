from django.test import TestCase, Client

"""
Test views
"""


class TestHomeView(TestCase):
    URL = "/"

    def setUp(self):
        self.client = Client()

    def test_should_return_200_when_app_is_running(self) -> None:
        response = self.client.get(TestHomeView.URL)

        self.assertEqual(response.status_code, 200)


class TestExercisesDetailView(TestCase):
    URL = "/palindrome"

    def setUp(self):
        self.client = Client()

    def test_should_return_301_when_palindrome_window_is_rendered(self) -> None:
        response = self.client.get(TestExercisesDetailView.URL)

        self.assertEqual(response.status_code, 301)


"""
Test models
"""
from exercises.models import Tasks, Tests


class TestTasksModel(TestCase):
    @classmethod
    def generateTestData(cls) -> None:
        record = Tasks(
            task_id=999, task_name="Test task", task_content="Test task content"
        )
        record.save()

    def setUp(self) -> None:
        self.generateTestData()
        self.test_task = Tasks.objects.get(task_id=999)

    def test_get_task_id(self) -> None:
        self.assertEqual(self.test_task.task_id, 999, msg="Task should be equal: 999")

    def test_task_title_content(self) -> None:
        expected_task_name = "Test task"

        self.assertEqual(
            self.test_task.task_name,
            expected_task_name,
            msg="Title should be 'Test task'",
        )

    def test_task_content(self) -> None:
        expected_task_content = "Test task content"

        self.assertEqual(
            self.test_task.task_content,
            expected_task_content,
            msg="Content should be 'Test task content'",
        )


class TestTestsModel(TestCase):
    @classmethod
    def generateTestData(cls):
        create_tasks_record = Tasks(
            task_id=999, task_name="Test task", task_content="Test task content"
        )
        create_tasks_record.save()

        tasks_record = Tasks.objects.get(task_id=999)

        tests_record = Tests(
            test_id=999,
            task_id=tasks_record,
            test_input="Hello",
            test_output="World",
            test_language="Python",
        )

        tests_record.save()

    def setUp(self) -> None:
        self.generateTestData()
        self.test_id = Tests.objects.get(test_id=999)

    def test_get_test_id(self) -> None:
        self.assertEqual(self.test_id.test_id, 999, msg="Test should be equal: 999")

    def test_test_input(self) -> None:
        expected_test_input = "Hello"

        self.assertEqual(
            self.test_id.test_input, expected_test_input, msg="Input should be 'Hello'"
        )

    def test_test_output(self) -> None:
        expected_test_output = "World"

        self.assertEqual(
            self.test_id.test_output,
            expected_test_output,
            msg="Output should be 'World'",
        )

    def test_test_output(self) -> None:
        expected_test_language = "Python"

        self.assertEqual(
            self.test_id.test_language,
            expected_test_language,
            msg="Language should be 'Python'",
        )
