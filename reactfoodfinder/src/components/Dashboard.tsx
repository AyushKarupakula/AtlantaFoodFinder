import React from 'react';
import styled from 'styled-components';
import { useAuth } from '../context/AuthContext';

const Dashboard: React.FC = () => {
  const { logout } = useAuth();

  return (
    <DashboardContainer>
      <DashboardHeader>My Account</DashboardHeader>
      <DashboardContent>
        <Section>
          <SectionTitle>Profile Information</SectionTitle>
          <ProfileInfo>
            <InfoItem>
              <Label>Name:</Label>
              <Value>John Doe</Value>
            </InfoItem>
            <InfoItem>
              <Label>Email:</Label>
              <Value>johndoe@example.com</Value>
            </InfoItem>
          </ProfileInfo>
        </Section>
        <Section>
          <SectionTitle>Recent Activity</SectionTitle>
          <ActivityList>
            <ActivityItem>Reviewed Restaurant A</ActivityItem>
            <ActivityItem>Favorited Restaurant B</ActivityItem>
            <ActivityItem>Searched for Italian cuisine</ActivityItem>
          </ActivityList>
        </Section>
        <LogoutButton onClick={logout}>Log Out</LogoutButton>
      </DashboardContent>
    </DashboardContainer>
  );
};

const DashboardContainer = styled.div`
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
`;

const DashboardHeader = styled.h1`
  font-size: 2rem;
  color: #333;
  margin-bottom: 2rem;
`;

const DashboardContent = styled.div`
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 2rem;
`;

const Section = styled.div`
  margin-bottom: 2rem;
`;

const SectionTitle = styled.h2`
  font-size: 1.5rem;
  color: #e74c3c;
  margin-bottom: 1rem;
`;

const ProfileInfo = styled.div``;

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

const ActivityList = styled.ul`
  list-style-type: none;
  padding: 0;
`;

const ActivityItem = styled.li`
  margin-bottom: 0.5rem;
  &:before {
    content: '•';
    color: #e74c3c;
    display: inline-block;
    width: 1em;
    margin-left: -1em;
  }
`;

const LogoutButton = styled.button`
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #c0392b;
  }
`;

export default Dashboard;