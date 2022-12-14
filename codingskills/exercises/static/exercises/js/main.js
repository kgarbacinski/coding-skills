/**
 * @fileoverview
 * Main JS file to handle POST requests to backend
 * and modify the layout in frontent.
 */

document.addEventListener("DOMContentLoaded", function() {
    const langButtons = document.getElementsByClassName("languages");
    const exerciseInput = document.getElementById('exercise_input');
    const exerciseOutput = document.getElementById('exercise_output');
    const submitButton = document.getElementById('submit_button');
    const taskCodeField = document.getElementById('task_code_field');
    const chosenLanguageField = document.getElementById('chosen_language');
    const csrfToken = generateCookie('csrftoken');
    const resultField = document.getElementById('result');
    const lastCursor = document.getElementById('last_cursor')

    const prepopulatedCode = {
        'Python': `def solution(value):
   #Type your code here:
   `,
        'Java': `class Solution {
    public static Boolean solution(String value) {
        // Type your code here:
      }
    }`,
        'Node': `function solution(value) {
    //Type your code here:

}

module.exports = { solution };`,
    }

    /**
     * @function
     * Reads the value from 'language' buttons
     * Set event listener on each button
     * Updates text_area with specific template based on auser decision
     * Calls sendData()
     */
    function updateViewWithLanguages() {
        let arrayed_buttons = Array.prototype.slice.call(langButtons);

        arrayed_buttons.forEach(element => {
            element.addEventListener('click', async function() {
                let language = element.id;
                chosenLanguageField.innerHTML = `Your solution in <span class='colored_text'>${language}</span>:`;
                taskCodeField.textContent = prepopulatedCode[language];
                await sendData(language);
            });
        });
    };

    /**
     * @function
     * @param {str} language
     *
     * POSTs the data collected from the view to the backend to host/checker/post/
     * Collects jsonified response from backend (sample: {'response': 'passed'})
     * Calls handleFrontEnd() and passes response
     */
    async function sendData(language) {
        submitButton.addEventListener('click', async function(event) {
            let postData = {
                'task_input': exerciseInput.textContent,
                'task_output': exerciseOutput.textContent,
                'task_code': taskCodeField.value,
                'task_language': language
            };

            let response = await fetch(`${window.origin}/checker/post/`, {
                body: JSON.stringify(postData),
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfToken
                }
            });

            let data = await response.json();
            handleFrontEnd(data);
        });
    };

    /**
     * @function
     * @param {str} data
     *
     * If data is avalable  renders & modifies result div
     * Applies CSS style based on the data content
     * After response is received and changes rendered, reloads the page after 5 seconds.
     */
    function handleFrontEnd(data) {
        console.log(data['response']);

        if (data['response']) {
            let result = data['response'];
            resultField.textContent += result;
            resultField.style.visibility = 'visible';
            lastCursor.classList.add('pause_animation');

            if (result == 'Passed') {
                resultField.classList.add('test_passed');
            } else {
                resultField.classList.add('test_failed');
            }
        }
        setTimeout(function() {
            location.reload();
        }, 5000);
    }

    /**
     * @function
     * @param {str} name
     * @returns str
     *
     * Supportive function to generate csrftoken.
     */
    function generateCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                };
            };
        };
        return cookieValue;
    };

    updateViewWithLanguages();
});
