const currentURL = window.location.href;

function addTask() {
        const inputElement = document.getElementById("newTaskInput");
        const inputValue = inputElement.value.trim();

        if (inputValue !== "") {
            const url = currentURL + "/add/" + encodeURIComponent(inputValue);
            const data = { task: inputValue };

            fetchTaskOperation(url, data);
        } else {
            alert("Please enter a task before adding.");
        }
    }

    function removeTask(task) {
        const inputValue = task.trim();

        if (inputValue !== "") {
            const url = currentURL + "/remove/" + encodeURIComponent(inputValue);
            const data = { task: inputValue };

            fetchTaskOperation(url, data);
        } else {
            alert("Please enter a task before removing.");
        }
    }

    function completeTask(task) {
        const inputValue = task.trim();

        if (inputValue !== "") {
            const url = currentURL + "/complete/" + encodeURIComponent(inputValue);
            const data = { task: inputValue };

            fetchTaskOperation(url, data);
        } else {
            alert("Please enter a task before completing.");
        }
    }

    function fetchTaskOperation(url, data) {
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Network response was not ok.');
        })
        .then(responseData => {
            // Handle the response as needed
            console.log(responseData);
            if (responseData.status === 'success') {
                window.location.reload();
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
    }



