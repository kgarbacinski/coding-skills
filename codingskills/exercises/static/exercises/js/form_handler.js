document.addEventListener("DOMContentLoaded", function() {
    const lang_buttons = document.getElementsByClassName("languages");
    const form = document.getElementById('form');
    const input = document.getElementById('code');

    function setListenersOnButtons() {
        let arrayed_buttons = Array.prototype.slice.call(lang_buttons);

        arrayed_buttons.forEach(element => {
            element.addEventListener('click', function() {
                let language = element.id;

                input.placeholder = `Add your solution in ${language}`;
                handleSend(language);

            });
        });
    }

    function handleSend(language) {
        form.addEventListener('submit', function(event) {
            const formData = new FormData(this);
            formData.append('test_lang', language);

            fetch(`${window.origin}/post`, {
                body: formData,
                method: 'POST'
            }).then(function(response) {
                response.json()
            }).then(function(data) {
                console.log(data);
            });
        });

    };

    setListenersOnButtons();
});