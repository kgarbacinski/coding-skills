from dataclasses import dataclass

@dataclass
class LanguageSpecs():
    code_validators = {
        'Python' : """from submitted_code import solution
from input_values import values

import os

input = values[0]
output = values[1]

def main():
    if solution(input) == output:
        os.environ['STATE'] = 'PASSED'
    os.environ['STATE'] = 'FAILED'



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
