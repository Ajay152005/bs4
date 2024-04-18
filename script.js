async function getRandomQuote() {
    const response = await fetch("https://api.quotable.io/random");
    const data = await response.json();
    displayQuote(data.content);
}

// function to display the quote on the webpage

function displayQuote(quote) {
    const quoteDisplay = document.getElementById("quoteDisplay");
    quoteDisplay.textContent = `${quote}`;
}