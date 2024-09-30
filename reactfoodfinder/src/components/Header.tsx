import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';
import { useAuth } from '../context/AuthContext';

const Header: React.FC = () => {
  const { isAuthenticated, logout } = useAuth();

  return (
    <HeaderContainer>
      <Logo>
        <LogoImage src="/logo.png" alt="AtlantaFoodFinder" />
        <LogoText>AtlantaFoodFinder</LogoText>
      </Logo>
      <SearchBar>
        <SearchInput type="text" placeholder="Search for restaurants or cuisines..." />
        <SearchButton>Search</SearchButton>
      </SearchBar>
      <Nav>
        <NavLink to="/">Home</NavLink>
        <NavLink to="/cuisines">Cuisines</NavLink>
        {isAuthenticated ? (
          <>
            <NavLink to="/account">My Account</NavLink>
            <LogoutButton onClick={logout}>Log Out</LogoutButton>
          </>
        ) : (
          <>
            <NavLink to="/login">Login</NavLink>
            <SignUpButton to="/signup">Sign Up</SignUpButton>
          </>
        )}
      </Nav>
    </HeaderContainer>
  );
};

const HeaderContainer = styled.header`
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 15px 20px;
  background-color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
`;

const Logo = styled.div`
  display: flex;
  align-items: center;
`;

const LogoImage = styled.img`
  height: 50px;
  margin-right: 15px;
`;

const LogoText = styled.span`
  font-size: 1.8rem;
  font-weight: bold;
  color: #e74c3c;
`;

const SearchBar = styled.div`
  display: flex;
  align-items: center;
  flex-grow: 1;
  margin: 0 30px;
`;

const SearchInput = styled.input`
  flex-grow: 1;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 4px 0 0 4px;
  font-size: 1rem;
`;

const SearchButton = styled.button`
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 0 4px 4px 0;
  cursor: pointer;
  font-size: 1rem;
  font-weight: bold;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #c0392b;
  }
`;

const Nav = styled.nav`
  display: flex;
  align-items: center;
`;

const NavLink = styled(Link)`
  color: #333;
  text-decoration: none;
  margin-left: 20px;
  font-size: 1rem;
  &:hover {
    color: #e74c3c;
  }
`;

const LogoutButton = styled.button`
  background: none;
  border: none;
  color: #333;
  font-size: 1rem;
  cursor: pointer;
  margin-left: 20px;
  &:hover {
    color: #e74c3c;
  }
`;

const SignUpButton = styled(Link)`
  background-color: #e74c3c;
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
  text-decoration: none;
  margin-left: 20px;
  font-size: 1rem;
  &:hover {
    background-color: #c0392b;
  }
`;

export default Header;