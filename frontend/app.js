// Connect to DOM elements
const boardDiv = document.getElementById('board');
const statusDiv = document.getElementById('status');

// Base URL for the backend API hosted on your EC2 instance
const API_BASE_URL = 'http://13.56.140.126:5000';

// Function to fetch some data from the backend API
async function fetchData() {
    try {
        const response = await fetch(`${API_BASE_URL}/data`); // Replace '/data' with the actual backend route
        if (response.ok) {
            const data = await response.json();
            statusDiv.innerText = `Data received: ${JSON.stringify(data)}`;
        } else {
            statusDiv.innerText = `Error: ${response.statusText}`;
        }
    } catch (error) {
        statusDiv.innerText = `Fetch failed: ${error.message}`;
    }
}

// Function to reset the board (or perform another action)
function resetBoard() {
    boardDiv.innerHTML = ''; // Clear the board content
    statusDiv.innerText = 'Board reset!';
    // Optionally, you can send a request to the backend to reset a game or state
}

// Initialize the page or attach event listeners
function init() {
    // Add event listeners, e.g., for buttons
    const resetButton = document.querySelector('button[onclick="resetBoard()"]');
    if (resetButton) {
        resetButton.addEventListener('click', resetBoard);
    }

    // Fetch initial data from the backend
    fetchData();
}

// Run the init function once the DOM content is loaded
document.addEventListener('DOMContentLoaded', init);

