const statusDiv = document.getElementById('status');

// Update the API_BASE_URL to point to the EC2 instance's public IP and backend port
const API_BASE_URL = 'http://54.241.84.38:5000';

async function fetchCryptoData() {
    try {
        // Use the updated API_BASE_URL
        const response = await fetch(`${API_BASE_URL}/crypto`);
        if (response.ok) {
            const data = await response.json();
            statusDiv.innerText = `
                Min Factor: ${data.min_factor}\n
                Min Path: ${JSON.stringify(data.min_path)}\n
                Max Factor: ${data.max_factor}\n
                Max Path: ${JSON.stringify(data.max_path)}
            `;
        } else {
            statusDiv.innerText = `Error: ${response.statusText}`;
        }
    } catch (error) {
        statusDiv.innerText = `Fetch failed: ${error.message}`;
    }
}

// Fetch the crypto data once the DOM is fully loaded
document.addEventListener('DOMContentLoaded', fetchCryptoData);

