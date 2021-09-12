from handlers import ContainerHandler, FilesHandler

class ExecuteTest:
    def __init__(self, input, output, code, language):
        self.__code = code
        self.__input = input
        self.__output = output
        self.__language = language
        self.__container_handler = ContainerHandler(self.__language)
        self.__files_handler = FilesHandler(self.__input, self.__output, self.__code, self.__language)

    def run_test(self):
        self.__container_handler.run_container()
        self.__files_handler.generate_all_files()
        self.__files_handler.copy_files_to_container()
        self.__container_handler.get_result_from_container()
        # self.__files_handler.remove_files()

# For testing purposes
#ExecuteTest(1, 2, 'def solution(value): return value * 2', 'Python').run_test()