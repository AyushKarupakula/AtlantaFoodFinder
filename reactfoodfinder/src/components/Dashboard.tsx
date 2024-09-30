import React from 'react';
import styled from 'styled-components';
import { useNavigate } from 'react-router-dom'; // Add this import
import { useAuth } from '../context/AuthContext';
import { FaUser, FaHistory, FaStar, FaHeart } from 'react-icons/fa';

const Dashboard: React.FC = () => {
  const { logout } = useAuth();
  const navigate = useNavigate(); // Add this line

  const handleLogout = () => {
    logout();
    navigate('/'); // This will redirect to the home page after logout
  };

  return (
    <DashboardContainer>
      <DashboardHeader>My Account</DashboardHeader>
      <CardGrid>
        <Card>
          <CardHeader>
            <FaUser />
            <CardTitle>Profile Information</CardTitle>
          </CardHeader>
          <CardContent>
            <InfoItem>
              <Label>Name:</Label>
              <Value>John Doe</Value>
            </InfoItem>
            <InfoItem>
              <Label>Email:</Label>
              <Value>johndoe@example.com</Value>
            </InfoItem>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <FaHistory />
            <CardTitle>Recent Activity</CardTitle>
          </CardHeader>
          <CardContent>
            <ActivityItem>
              <FaStar /> Reviewed Restaurant A
            </ActivityItem>
            <ActivityItem>
              <FaHeart /> Favorited Restaurant B
            </ActivityItem>
            <ActivityItem>
              <FaHistory /> Searched for Italian cuisine
            </ActivityItem>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <FaStar />
            <CardTitle>Favorite Restaurants</CardTitle>
          </CardHeader>
          <CardContent>
            <FavoriteItem>Restaurant X</FavoriteItem>
            <FavoriteItem>Restaurant Y</FavoriteItem>
            <FavoriteItem>Restaurant Z</FavoriteItem>
          </CardContent>
        </Card>
      </CardGrid>
      <LogoutButton onClick={handleLogout}>Log Out</LogoutButton>
    </DashboardContainer>
  );
};

const DashboardContainer = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
`;

const DashboardHeader = styled.h1`
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 2rem;
  text-align: center;
`;

const CardGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
`;

const Card = styled.div`
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: transform 0.3s ease;

  &:hover {
    transform: translateY(-5px);
  }
`;

const CardHeader = styled.div`
  background-color: #e74c3c;
  color: white;
  padding: 1rem;
  display: flex;
  align-items: center;

  svg {
    margin-right: 0.5rem;
    font-size: 1.2rem;
  }
`;

const CardTitle = styled.h2`
  font-size: 1.2rem;
  margin: 0;
`;

const CardContent = styled.div`
  padding: 1.5rem;
`;

const InfoItem = styled.div`
  display: flex;
  margin-bottom: 0.5rem;
`;

const Label = styled.span`
  font-weight: bold;
  width: 100px;
`;

const Value = styled.span`
  flex-grow: 1;
`;

const ActivityItem = styled.div`
  display: flex;
  align-items: center;
  margin-bottom: 0.5rem;

  svg {
    margin-right: 0.5rem;
    color: #e74c3c;
  }
`;

const FavoriteItem = styled.div`
  background-color: #f8f8f8;
  border-radius: 5px;
  padding: 0.5rem;
  margin-bottom: 0.5rem;
`;

const LogoutButton = styled.button`
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
  display: block;
  margin: 0 auto;

  &:hover {
    background-color: #c0392b;
  }
`;

export default Dashboard;