import os
import shutil

from .language_specs import LanguageSpecs

class ContainerHandler:
    def __init__(self, language, container_name):
        self.__language_specs = LanguageSpecs()
        self.__language = language
        self.__file_extension = self.__language_specs.language_extensions.get(self.__language)
        self.__imageURL = f'dyeroshenko/coding_challenges_{self.__file_extension}_env'
        self.__container_name = container_name

    def run_container(self):
        start_container = f'docker run -d --name {self.__container_name} -v $PWD/checker/temp/result_files:/result {self.__imageURL} sleep 100'
        os.system(start_container)

    def run_compiler(self):
        compilers = self.__language_specs.language_compilers.get(self.__language)

        for compiler in compilers:
            os.system(f"docker exec -d {self.__container_name} {compiler} -u /test/code_validator.{self.__file_extension}")

    def stop_container(self):
        stop_container = f'docker kill {self.__container_name} && docker rm {self.__container_name}'
        os.system(stop_container)


class FilesHandler:
    def __init__(self, input, output, code, language, container_name):
        self.__input = input
        self.__output = output
        self.__code = code
        self.__language = language
        self.__language_specs = LanguageSpecs()
        self.__file_extension = self.__language_specs.language_extensions.get(self.__language)
        self.__code_validator = open(self.__language_specs.code_validators.get(self.__language), "r").read()
        self.__exec_folder_path = os.path.join(os.getcwd(), f'checker/temp/exec_files/{self.__file_extension}/')
        self.__result_folder_path = os.path.join(os.getcwd(), f'checker/temp/result_files/')
        self.__container_name = container_name

    def __generate_code_validation_file(self):
        file_name = f'{self.__exec_folder_path}/code_validator.{self.__file_extension}'

        with open(file_name, 'w') as file:
            file.write(self.__code_validator)

    def __generate_submitted_code_file(self):
        file_name = f'{self.__exec_folder_path}/submitted_code.{self.__file_extension}'

        with open(file_name, 'w') as file:
            file.write(self.__code)

    def __generate_testing_values_file(self):
        values = f'{{\n  "input": "{self.__input}",\n  "output": "{self.__output}"\n}}'
        file_name = f'{self.__exec_folder_path}/input_values.json'
        
        with open(file_name, 'w') as file:
            file.write(values)

    def generate_all_files(self):
        os.mkdir(self.__exec_folder_path)
        self.__generate_code_validation_file()
        self.__generate_submitted_code_file()
        self.__generate_testing_values_file()

    def copy_files_to_container(self):
        copy_files_to_container = f'docker cp {self.__exec_folder_path} {self.__container_name}:test'
        os.system(copy_files_to_container)

    def copy_result_from_container(self):
        get_generated_result = f'docker cp {self.__container_name}:/result/result_{self.__file_extension}.txt {self.__result_folder_path}'
        os.system(get_generated_result)

    def get_result_value(self):
        file_path = f'checker/temp/result_files/result_{self.__file_extension}.txt'

        with open(file_path, 'r') as file:
            result = file.read()
            return result

    def cleanup_temp_files(self):
        shutil.rmtree(self.__exec_folder_path)
        shutil.rmtree(self.__result_folder_path)