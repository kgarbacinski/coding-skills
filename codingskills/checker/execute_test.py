from .handlers import ContainerHandler, FilesHandler
import uuid

class ExecuteTest:
    def __init__(self, input, output, code, language):
        self.__code = code
        self.__input = input
        self.__output = output
        self.__language = language
        self.__container_name = uuid.uuid1()
        self.__container_handler = ContainerHandler(self.__language, self.__container_name)
        self.__files_handler = FilesHandler(self.__input, self.__output, self.__code, self.__language, self.__container_name)

    def run_test(self):
        self.__container_handler.run_container()
        self.__files_handler.generate_all_files()
        self.__files_handler.copy_files_to_container()
        self.__container_handler.run_compiler()
        self.__files_handler.copy_result_from_container()
        test_result = self.__files_handler.get_result_value()
        self.__container_handler.stop_container()
        self.__files_handler.cleanup_temp_files()

        return test_result