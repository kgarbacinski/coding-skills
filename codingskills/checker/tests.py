from django.test import TestCase
from unittest.mock import patch

from checker.handlers import ContainerHandler, FilesHandler

'''
Handlers functionality tests
'''
class TestContainerHandler(TestCase):
    def setUp(self) -> None:
        self.container_handler = ContainerHandler(language='node', container_name='NAME')

    @patch('os.system')
    def test_should_return_correct_docker_run_command(self, mock_os)-> None:
        self.container_handler.run_container()
        command = 'docker run -d --name NAME -v $PWD/checker/temp/result_files:/result dyeroshenko/coding_challenges_js_env sleep 1000'
        
        mock_os.assert_called_with(command)

    @patch('os.system')
    def test_should_return_correct_compile_command(self, mock_os)-> None:
        self.container_handler.run_compiler()
        command = "docker exec -d NAME node /js_image/exec_files/Validator.js"

        mock_os.assert_called_with(command)

    @patch('os.system')
    def test_should_return_correct_container_stop_command(self, mock_os)-> None:
        self.container_handler.stop_container()
        command = "docker stop NAME && docker rm NAME"

        mock_os.assert_called_with(command)


class TestFilesHandler(TestCase):
    def setUp(self)-> None:
        self.files_handler = FilesHandler(
            input='hello', 
            output='world', 
            code='console.log("hello")',
            language = 'node', 
            container_name = 'abc'
            )

    @patch('builtins.open')
    @patch('os.mkdir')
    def test_should_generate_all_files(self, open, mk_dir) -> None:
        self.files_handler.generate_all_files()

        open.assert_called_once()

    @patch('os.system')
    def test_should_call_copy_to_container_command(self, mock_os) -> None:
        self.files_handler.copy_files_to_container()

        mock_os.assert_called_once()

    @patch('os.system')
    def test_should_call_correct_copy_result_from_container_command(self, mock_os) -> None:
        self.files_handler.copy_result_from_container()

        mock_os.assert_called_once()

    @patch('builtins.open')
    def test_should_read_result_value_from_file(self, open) -> None:
        self.files_handler.get_result_value()

        open.assert_called_once()

    @patch('shutil.rmtree')
    def test_should_call_copy_to_container_command(self, shutil) -> None:
        self.files_handler.cleanup_temp_files()

        self.assertEqual(shutil.call_count, 2)

    
'''
execute_test functionality tests
'''
from checker.execute_test import ExecuteTest

class TestExecuteTest(TestCase):
    def setUp(self) -> None:
        self.execute_test = ExecuteTest(
            input='hello', 
            output='world', 
            code='console.log("hello")',
            language = 'node' 
            )

    def test_should_return_correct_instance_of_container_handler(self) -> None: 
        self.assertIsInstance(self.execute_test.container_handler, ContainerHandler)

    def test_should_return_correct_instance_of_files_handler_handler(self) -> None: 
        self.assertIsInstance(self.execute_test.files_handler, FilesHandler)

    @patch('checker.execute_test.ExecuteTest.run_test')
    def test_should_check_if_run_test_not_called(self, mock_run_test) -> None:
        mock_run_test.assert_not_called()