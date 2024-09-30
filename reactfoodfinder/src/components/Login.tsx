import React, { useState } from 'react';
import styled from 'styled-components';
import { Link, useNavigate } from 'react-router-dom';

const Login: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Login attempted with:', email, password);
    // Here you would typically perform authentication
    // For now, we'll just redirect to the home page
    navigate('/');
  };

  return (
    <LoginContainer>
      <ImageSection>
        <h1>Atlanta Food Finder</h1>
        <p>Discover the best restaurants in Atlanta</p>
      </ImageSection>
      <FormSection>
        <LoginWrapper>
          <LoginForm onSubmit={handleSubmit}>
            <LoginHeader>Welcome Back</LoginHeader>
            <InputGroup>
              <StyledInput
                type="email"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                placeholder="Email"
              />
            </InputGroup>
            <InputGroup>
              <StyledInput
                type="password"
                id="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                placeholder="Password"
              />
            </InputGroup>
            <SubmitButton type="submit">Sign In</SubmitButton>
          </LoginForm>
          <SignUpPrompt>
            Don't have an account? <Link to="/signup">Sign up here</Link>
          </SignUpPrompt>
        </LoginWrapper>
      </FormSection>
    </LoginContainer>
  );
};

const LoginContainer = styled.div`
  display: flex;
  height: 100vh;

  @media (max-width: 768px) {
    flex-direction: column;
  }
`;

const ImageSection = styled.div`
  flex: 1;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: white;
  padding: 2rem;
  text-align: center;

  h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }

  p {
    font-size: 1.2rem;
  }

  @media (max-width: 768px) {
    padding: 1rem;
  }
`;

const FormSection = styled.div`
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f7fafc;

  @media (max-width: 768px) {
    padding: 1rem;
  }
`;

const LoginWrapper = styled.div`
  background-color: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
`;

const LoginForm = styled.form`
  margin-bottom: 1rem;
`;

const LoginHeader = styled.h2`
  text-align: center;
  color: #333;
  margin-bottom: 2rem;
  font-size: 2rem;
`;

const InputGroup = styled.div`
  margin-bottom: 1.5rem;
`;

const StyledInput = styled.input`
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  transition: border-color 0.3s ease;

  &:focus {
    outline: none;
    border-color: #667eea;
  }
`;

const SubmitButton = styled.button`
  width: 100%;
  padding: 0.75rem;
  background-color: #667eea;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #5a67d8;
  }
`;

const SignUpPrompt = styled.p`
  text-align: center;
  font-size: 0.9rem;
  color: #333;

  a {
    color: #667eea;
    text-decoration: none;
    font-weight: bold;
  }
`;

export default Login;
