document.addEventListener("DOMContentLoaded", () => {
    const jokeContainer = document.getElementById("joke");
    const btn = document.getElementById("btn");
    const url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single";

    let getJoke = () => {
        jokeContainer.classList.remove("fade");
        fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.joke) {
                jokeContainer.textContent = data.joke;
            } else {
                jokeContainer.textContent = "Failed to fetch a joke.";
            }
            jokeContainer.classList.add("fade");
        })
        .catch(error => {
            jokeContainer.textContent = "An error occurred while fetching the joke.";
            jokeContainer.classList.add("fade");
        });
    };

    btn.addEventListener("click", getJoke);
    getJoke();
});
