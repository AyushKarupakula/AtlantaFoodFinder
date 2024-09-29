import React, { useState } from 'react';
import styled, { keyframes } from 'styled-components';
import atlantaFoodImage from '/Users/ayushkarupakula/AtlantaFoodFinder/reactfoodfinder/src/components/assets/atlanta-food.jpg'; // Make sure to add this image to your assets folder

const SignUp: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      alert("Passwords don't match!");
      return;
    }
    console.log('Sign up attempted with:', email, password);
  };

  return (
    <SignUpContainer>
      <ImageSection>
        <Overlay />
        <WelcomeText>
          <h1>Discover Atlanta's Culinary Delights</h1>
          <p>Join us to explore the best restaurants in the city</p>
        </WelcomeText>
      </ImageSection>
      <FormSection>
        <SignUpForm onSubmit={handleSubmit}>
          <Logo>AtlantaFoodFinder</Logo>
          <h2>Create Your Account</h2>
          <InputGroup>
            <Label htmlFor="email">Email</Label>
            <Input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </InputGroup>
          <InputGroup>
            <Label htmlFor="password">Password</Label>
            <Input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </InputGroup>
          <InputGroup>
            <Label htmlFor="confirm-password">Confirm Password</Label>
            <Input
              type="password"
              id="confirm-password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
            />
          </InputGroup>
          <SubmitButton type="submit">Sign Up</SubmitButton>
        </SignUpForm>
      </FormSection>
    </SignUpContainer>
  );
};

const fadeIn = keyframes`
  from { opacity: 0; }
  to { opacity: 1; }
`;

const SignUpContainer = styled.div`
  display: flex;
  min-height: 100vh;
  animation: ${fadeIn} 0.5s ease-in;
`;

const ImageSection = styled.div`
  flex: 1.2;
  background-image: url(${atlantaFoodImage});
  background-size: cover;
  background-position: center;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
`;

const Overlay = styled.div`
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(255, 99, 71, 0.7), rgba(255, 165, 0, 0.7));
`;

const WelcomeText = styled.div`
  position: relative;
  color: white;
  text-align: center;
  max-width: 80%;

  h1 {
    font-size: 3.5rem;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
  }

  p {
    font-size: 1.4rem;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
  }
`;

const FormSection = styled.div`
  flex: 0.8;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #f8f9fa, #e9ecef);
  padding: 2rem;
`;

const Logo = styled.div`
  font-size: 2rem;
  font-weight: bold;
  background: linear-gradient(45deg, #ff6347, #ff8c00);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 2rem;
  text-align: center;
`;

const SignUpForm = styled.form`
  background-color: white;
  padding: 3rem;
  border-radius: 15px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;

  h2 {
    text-align: center;
    color: #333;
    margin-bottom: 2rem;
    font-size: 2rem;
  }
`;

const InputGroup = styled.div`
  margin-bottom: 1.5rem;
`;

const Label = styled.label`
  display: block;
  margin-bottom: 0.5rem;
  color: #555;
  font-weight: 500;
`;

const Input = styled.input`
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.3s ease;

  &:focus {
    outline: none;
    border-color: #ff6347;
    box-shadow: 0 0 0 3px rgba(255, 99, 71, 0.2);
  }
`;

const SubmitButton = styled.button`
  width: 100%;
  padding: 0.75rem;
  background: linear-gradient(45deg, #ff6347, #ff8c00);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    background: linear-gradient(45deg, #ff4500, #ff7f00);
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(255, 99, 71, 0.3);
  }

  &:active {
    transform: translateY(0);
  }
`;

export default SignUp;