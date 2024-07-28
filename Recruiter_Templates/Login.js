document.getElementById('createAccountLink').addEventListener('click', function() {
    document.querySelector('.login-form').style.display = 'none';
    document.querySelector('.signup-form').style.display = 'block';
});

document.getElementById('loginLink').addEventListener('click', function() {
    document.querySelector('.signup-form').style.display = 'none';
    document.querySelector('.login-form').style.display = 'block';
});

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    console.log('Logging in with:', email, password);
    // Add your login logic here
});

document.getElementById('createForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('newEmail').value;
    const password = document.getElementById('newPassword').value;
    console.log('Creating account with:', email, password);
    // Add your account creation logic here
});
