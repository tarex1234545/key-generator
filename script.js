// Function to generate a random 8-digit key
function generateKey() {
    let keyLength = 8; // Fixed length for the key
    let key = '';
    const characters = '0123456789'; // Numeric characters for the key

    // Generate the key
    for (let i = 0; i < keyLength; i++) {
        key += characters.charAt(Math.floor(Math.random() * characters.length));
    }

    // Display the generated key
    document.getElementById('generatedKey').textContent = `Generated Key: ${key}`;
}

// Function to clear the generated key
function clearKey() {
    document.getElementById('generatedKey').textContent = '';
}

// Attach event listeners to buttons
document.getElementById('generateKeyBtn').addEventListener('click', generateKey);
document.getElementById('clearBtn').addEventListener('click', clearKey);
