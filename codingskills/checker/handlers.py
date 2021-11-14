import os
import shutil
import time

from .language_specs import LanguageSpecs

class ContainerHandler:
    def __init__(self, language, container_name):
        self.__language_specs = LanguageSpecs()
        self.__language = language
        self.__file_extension = self.__language_specs.language_extensions.get(self.__language)
        self.__imageURL = f'dyeroshenko/coding_challenges_{self.__file_extension}_env'
        self.__container_name = container_name

    def run_container(self):
        start_container = f'docker run -d --name {self.__container_name} -v $PWD/checker/temp/result_files:/result {self.__imageURL} sleep 1000'
        os.system(start_container)
        print(f'====> Started container: {self.__container_name}')

    def run_compiler(self):
        compilers = self.__language_specs.language_compilers.get(self.__language)

        for index, compiler in enumerate(compilers):
            if index > 0:
                task = f"docker exec -d {self.__container_name} {compiler} /{self.__file_extension}_image/exec_files/Validator"
                os.system(task)
                print(f'====> Run task: {task}')
            else:
                task = f"docker exec -d {self.__container_name} {compiler} /{self.__file_extension}_image/exec_files/Validator.{self.__file_extension}"
                os.system(task)
                print(f'====> Run task: {task}')

    def stop_container(self):
        stop_container = f'docker stop {self.__container_name} && docker rm {self.__container_name}'
        os.system(stop_container)
        print(f'====> Container stopped & removed: {self.__container_name}')


class FilesHandler:
    def __init__(self, input, output, code, language, container_name):
        self.__input = input
        self.__output = output
        self.__code = code
        self.__language = language
        self.__language_specs = LanguageSpecs()
        self.__file_extension = self.__language_specs.language_extensions.get(self.__language)
        self.__code_validator = open(self.__language_specs.code_validators.get(self.__language), 'r').read()
        self.__xml_template = open(self.__language_specs.xml_template, 'r').read()
        self.__exec_folder_path = os.path.join(os.getcwd(), f'checker/temp/exec_files')
        self.__result_folder_path = os.path.join(os.getcwd(), f'checker/temp/result_files')
        self.__container_name = container_name

    def __generate_code_validation_file(self):
        file_name = f'{self.__exec_folder_path}/Validator.{self.__file_extension}'

        with open(file_name, 'w+') as file:
            file.write(self.__code_validator)

        print('====> Created [code_validation_file]')

    def __generate_submitted_code_file(self):
        file_name = f'{self.__exec_folder_path}/Solution.{self.__file_extension}'

        with open(file_name, 'w+') as file:
            file.write(self.__code)

        print('====> Created [submitted_code_file]')

    def __generate_testing_values_file(self):
        values = self.__xml_template.replace(
            'INPUT_VALUE', self.__input).replace(
                'OUTPUT_VALUE', self.__output)
                
        file_name = f'{self.__exec_folder_path}/input_values.xml'
        
        with open(file_name, 'w+') as file:
            file.write(values)

        print('====> Created [values_file]')

    def generate_all_files(self):
        os.mkdir(self.__exec_folder_path)
        self.__generate_code_validation_file()
        self.__generate_submitted_code_file()
        self.__generate_testing_values_file()

        print('====> All files are generated')

    def copy_files_to_container(self):
        copy_files_to_container = f'docker cp {self.__exec_folder_path} {self.__container_name}:{self.__file_extension}_image'
        os.system(copy_files_to_container)

        print('====> Files added to container')

    def copy_result_from_container(self):
        get_generated_result = f'docker cp {self.__container_name}:/{self.__file_extension}_image/exec_files/result_{self.__file_extension}.txt {self.__result_folder_path}'
        os.system(get_generated_result)

        print('====> Files copied from container')

    def get_result_value(self):
        print('====> Trying to read result from container')
        file_path = f'checker/temp/result_files/result_{self.__file_extension}.txt'

        try: 
            with open(file_path, 'r') as file:
                result = file.read()
                print(f'====> Result is available: {result}')
                return result
        except FileNotFoundError:
            print(f'====> Code was not compiled in container.')
            return 'unable to compile'

    def cleanup_temp_files(self):
        time.sleep(3)
        shutil.rmtree(self.__exec_folder_path)
        shutil.rmtree(self.__result_folder_path)
        print('====> Files are removed')