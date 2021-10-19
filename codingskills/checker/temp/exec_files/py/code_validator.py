from submitted_code import solution
import json

def get_input_values():
    file = open('input_values.json')
    data = json.load(file)

    input = data['input']
    output = data['output']

    return input, output
    
def checker():
    input = get_input_values()[0]
    output = get_input_values()[1]

    result = ''
    if str(solution(input)) == output:
        result = 'Passed'
    else:
        result = 'Failed'

    return result

def file_generator():
    result = checker()

    with open('/result/result_py.txt', 'w') as file:
            file.write(result)


if __name__ == '__main__':
    file_generator()