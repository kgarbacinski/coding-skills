from dataclasses import dataclass

@dataclass
#Config file with codfe per language
class LanguageSpecs():
    code_validators = {
        #Add file writing functionality to this file & save to JSON
        'Python' : """from submitted_code import solution
from input_values import values

import os

input = values[0]
output = values[1]

def main():
    result = ''
    if solution(input) == output:
        result = 'Passed'
    else:
        result = 'Failed'

    


if __name__ == '__main__':
    main()
"""
    }

    language_extensions = {
        'Python' : 'py',
        'Java': 'java',
        'NodeJS': 'js'
    }

    language_compilers = {
        'Python': 'python3'
    }
