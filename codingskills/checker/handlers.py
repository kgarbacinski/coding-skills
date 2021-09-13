import os
import shutil

from language_specs import LanguageSpecs

class ContainerHandler(LanguageSpecs):
    def __init__(self, language, container_name):
        self.__language = language
        self.__file_extension = self.language_extensions.get(self.__language)
        self.__language_compiler = self.language_compilers.get(self.__language)
        self.__imageURL = f'dyeroshenko/coding_challenges_{self.__file_extension}_env'
        self.__container_name = container_name

    def run_container(self):
        start_container = f'docker run -d --name {self.__container_name} {self.__imageURL} sleep 1000'
        os.system(start_container)

    def get_result_from_container(self):
        run_generated_file = f'docker exec {self.__container_name} {self.__language_compiler} /test/code_validator.{self.__file_extension}'
        get_result = f'docker logs {self.__container_name}'
        os.system(run_generated_file)
        os.system(get_result)

    def stop_container(self):
        stop_container = f'docker kill {self.__container_name}'
        os.system(stop_container)



class FilesHandler(LanguageSpecs):
    def __init__(self, input, output, code, language, container_name):
        self.__input = input
        self.__output = output
        self.__code = code
        self.__language = language
        self.__file_extension = self.language_extensions.get(self.__language)
        self.__code_validator = self.code_validators.get(self.__language)
        self.__folder_path = os.path.join(os.getcwd(), f'checker/exec_files/{self.__file_extension}')
        self.__container_name = container_name

    def __generate_code_validation_file(self):
        file_name = f'{self.__folder_path}/code_validator.{self.__file_extension}'

        with open(file_name, 'w') as file:
            file.write(self.__code_validator)

    def __generate_submitted_code_file(self):
        file_name = f'{self.__folder_path}/submitted_code.{self.__file_extension}'

        with open(file_name, 'w') as file:
            file.write(self.__code)

    def __generate_testing_values_file(self):
        values = f"values = [{self.__input}, {self.__output}]"
        file_name = f'{self.__folder_path}/input_values.{self.__file_extension}'
        
        with open(file_name, 'w') as file:
            file.write(values)

    def generate_all_files(self):
        os.mkdir(self.__folder_path)
        self.__generate_code_validation_file()
        self.__generate_submitted_code_file()
        self.__generate_testing_values_file()

    def copy_files_to_container(self):
        copy_files_to_container = f'docker cp {self.__folder_path} {self.__container_name}:test'
        os.system(copy_files_to_container)
        pass

    def remove_files(self):
        shutil.rmtree(self.__folder_path)