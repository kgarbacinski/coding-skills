from django.test import TestCase
from checker.handlers import ContainerHandler, FilesHandler
from language_specs import LanguageSpecs

class TestContainerHandler(TestCase):
    def setUp(self):
        self.container_handler = ContainerHandler('node', 'abc')

    def test_should_return_correct_docker_run_command(self)-> None:
        self.assertEqual(
            self.container_handler.run_container.start_container, 
            'docker run -d --name abc -v $PWD/checker/temp/result_files:/result dyeroshenko/coding_challenges_js_env sleep 1000'           
            )