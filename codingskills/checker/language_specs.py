from dataclasses import dataclass

@dataclass(frozen=True)
class LanguageSpecs():
    code_validators = {
        'python': 'checker/configs/py.txt',
        'java': 'checker/configs/java.txt'
    }

    xml_template = 'checker/configs/xml_template.txt'

    language_extensions = {
        'python': 'py',
        'java': 'java',
        'c++': 'cpp',
        'nodejs': 'js'
    }

    language_compilers = {
        'python': ['python3'],
        'java': ['javac', 'java']
    }