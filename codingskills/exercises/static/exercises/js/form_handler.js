document.addEventListener("DOMContentLoaded", function() {
    const lang_buttons = document.getElementsByClassName("languages");
    const exercise_input = document.getElementById('exercise_input');
    const exercise_output = document.getElementById('exercise_output');
    const submit_button = document.getElementById('submit_button');
    const task_code_field = document.getElementById('task_code_field');
    const csrftoken = getCookie('csrftoken');


    function setListenersOnButtons() {
        let arrayed_buttons = Array.prototype.slice.call(lang_buttons);

        arrayed_buttons.forEach(element => {
            element.addEventListener('click', function() {
                let language = element.id;
                task_code_field.placeholder = `Your solution in ${language}:`;
                handleSend();

            });
        });
    }

    function handleSend() {
        submit_button.addEventListener('click', function(event) {
            let postData = {
                'task_input': exercise_input.textContent,
                'task_output': exercise_output.textContent,
                'task_code': task_code_field.value
            }
            fetch(`${window.origin}/checker/post/`, {
                body: JSON.stringify(postData),
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrftoken
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
                }
            }
        }
        return cookieValue;
    }

    setListenersOnButtons();
});