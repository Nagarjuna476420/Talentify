// src/Login.js

import React from 'react';
import { useForm } from 'react-hook-form';
import './Login.css';

const Login = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = (data) => {
    console.log(data);
    // Handle login logic here
  };

  const handleCreateAccount = () => {
    // Redirect to the create account page or open a modal, etc.
    // For now, we'll just log a message
    console.log('Redirect to create account page');
  };

  return (
    <div className="login-container">
      <h2>Recruiter Login</h2>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="form-group">
          <label htmlFor="email">Email :
          <input
            id="email"
            type="email"
            {...register('email', {
              required: 'Email is required',
              pattern: {
                value: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
                message: 'Invalid email address',
              },
            })}
          /></label>
          {errors.email && <p className="error-message">{errors.email.message}</p>}
        </div>

        <div className="form-group">
          <label htmlFor="password">Password :
          <input
            id="password"
            type="password"
            {...register('password', {
              required: 'Password is required',
              minLength: {
                value: 6,
                message: 'Password must be at least 6 characters long',
              },
            })}
          /></label>
          {errors.password && <p className="error-message">{errors.password.message}</p>}
        </div>

        <button type="submit" className="login-button">Login</button>
      </form>

      <div className="create-account">
        <p>Don't have an account?</p>
        <button onClick={handleCreateAccount} className="create-account-button">Create Account</button>
      </div>
    </div>
  );
};

export default Login;
