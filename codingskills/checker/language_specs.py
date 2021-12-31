from dataclasses import dataclass


@dataclass(frozen=True)
class LanguageSpecs():
    """
    This class is used to store path to config files & language specific extensions / commands.
    
    Callers: 
        ContainerHandler
        FilesHandler
    """
    code_validators = {
        'python': 'checker/configs/py.txt',
        'java': 'checker/configs/java.txt',
        'node': 'checker/configs/nodejs.txt'
    }

    language_extensions = {
        'python': 'py',
        'java': 'java',
        'node': 'js'
    }

    language_compilers = {
        'python': ['python3'],
        'java': ['javac', 'java'],
        'node': ['node']
    }

    xml_template = 'checker/configs/xml_template.txt'