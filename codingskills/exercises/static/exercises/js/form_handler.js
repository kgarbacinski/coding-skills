document.addEventListener("DOMContentLoaded", function() {
    const langButtons = document.getElementsByClassName("languages");
    const exerciseInput = document.getElementById('exercise_input');
    const exerciseOutput = document.getElementById('exercise_output');
    const submitButton = document.getElementById('submit_button');
    const taskCodeField = document.getElementById('task_code_field');
    const chosenLanguageField = document.getElementById('chosen_language');
    const csrfToken = getCookie('csrftoken');

    const prepopulatedCode = {
        'Python': `def solution(value):
   #Add your code below:
   `,
        'Java': 'Java support will be added soon. Try Python first!',
        'C++': 'Java support will be added soon. Try Python first!',
        'JavaScript': 'Java support will be added soon. Try Python first!',
    }


    function updateViewWithLanguage() {
        let arrayed_buttons = Array.prototype.slice.call(langButtons);

        arrayed_buttons.forEach(element => {
            element.addEventListener('click', function() {
                let language = element.id;
                chosenLanguageField.textContent = `Your solution in ${language}:`;
                taskCodeField.textContent = prepopulatedCode[language];
                handleSend(language);
            });
        });
    };

    function handleSend(language) {
        submitButton.addEventListener('click', function(event) {
            let postData = {
                'task_input': exerciseInput.textContent,
                'task_output': exerciseOutput.textContent,
                'task_code': task_code_field.value,
                'task_language': language
            };
            fetch(`${window.origin}/checker/post/`, {
                body: JSON.stringify(postData),
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfToken
                }
            }).then(function(response) {
                console.log(response);
            });
        });

    };

    function getCookie(name) {
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

    updateViewWithLanguage();
});