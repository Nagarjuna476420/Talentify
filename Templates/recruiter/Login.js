document.addEventListener('DOMContentLoaded', () => {
    // Example CSRF token, in a real scenario you would retrieve this from your server
    const csrfToken = 'your-csrf-token-here';

    // Add CSRF token to forms
    document.getElementById('csrf-token').value = csrfToken;
    document.getElementById('csrf-token-create').value = csrfToken;
});
