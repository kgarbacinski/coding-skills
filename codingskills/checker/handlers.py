import os
import shutil

from language_specs import LanguageSpecs

class ExecuteTest:
    def __init__(self, input, output, code, language):
        self.code = code
        self.input = input
        self.output = output
        self.language = language
        self.container_handler = ContainerHandler(self.language)
        self.files_handler = FilesHandler(self.input, self.output, self.code, self.language)

    def run_test(self):
        self.container_handler.run_container()
        self.files_handler.generate_all_files()
        self.files_handler.copy_files_to_container()
        self.container_handler.get_result_from_container()
        self.files_handler.remove_files()



class ContainerHandler(LanguageSpecs):
    def __init__(self, language):
        self.language = language
        self.file_extension = self.language_extensions.get(self.language)
        self.containerURL = f'url/path/to/container/{self.file_extension}_env'

    def run_container(self):
        #bash command to run container here
        #self.id_cointainer = 'docker command to get container_id'
        #self.get_result_from_container()
        print('Running imaginary container!')

    def get_result_from_container(self):
        print('Look at these awesome results!')
        #docker exec <container> bash -c "python3 code_validator code, input, output"


class FilesHandler(LanguageSpecs):
    def __init__(self, input, output, code, language):
        self.input = input
        self.output = output
        self.code = code
        self.language = language
        self.file_extension = self.language_extensions.get(self.language)
        self.code_validator = self.code_validators.get(self.language)
        self.folder_path = os.path.join(os.getcwd(), f'checker/exec_files/{self.file_extension}')

    def generate_code_validation_file(self):
        file_name = f'{self.folder_path}/code_validator.{self.file_extension}'

        with open(file_name, 'w') as file:
            file.write(self.code_validator)

    def generate_submitted_code_file(self):
        file_name = f'{self.folder_path}/submitted_code.{self.file_extension}'

        with open(file_name, 'w') as file:
            file.write(self.code)

    def generate_testing_values_file(self):
        values = f"values = [{self.input}, {self.output}]"
        file_name = f'{self.folder_path}/input_values.{self.file_extension}'
        
        with open(file_name, 'w') as file:
            file.write(values)

    def generate_all_files(self):
        os.mkdir(self.folder_path)
        self.generate_code_validation_file()
        self.generate_submitted_code_file()
        self.generate_testing_values_file()

    def copy_files_to_container(self):
        print('Moving files to imaginary container!')

    def remove_files(self):
        shutil.rmtree(self.folder_path)


# For testing purposes
#ExecuteTest(1, 2, 'def solution(value): return value * 2', 'Python').run_test()
