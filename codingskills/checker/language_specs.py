from dataclasses import dataclass

@dataclass(frozen=True)
class LanguageSpecs():
    code_validators = {
        'python': 'checker/configs/py.txt',
        'java': 'checker/configs/java.txt',
        'nodejs': 'checker/configs/nodejs.txt'
    }

    language_extensions = {
        'python': 'py',
        'java': 'java',
        'nodejs': 'js'
    }

    language_compilers = {
        'python': ['python3'],
        'java': ['javac', 'java'],
        'nodejs': ['node']
    }

    xml_template = 'checker/configs/xml_template.txt'