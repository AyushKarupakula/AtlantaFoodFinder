# AtlantaFoodFinder

AtlantaFoodFinder is a web application that helps users discover and explore restaurants in Atlanta, Georgia. It features a Django backend API and a React frontend.

## Features

- Browse restaurants by cuisine type
- Search for restaurants by name or location
- View restaurant details, including menu, hours, and reviews
- User authentication and profile management
- Add and manage favorite restaurants

## Project Structure

- `backend/`: Django backend API
  - `atlantafoodfinder/`: Main Django project directory
  - `restaurants/`: Django app for restaurant-related functionality
  - `users/`: Django app for user authentication and profiles
- `reactfoodfinder/`: React frontend application

## Installation and Setup

### Backend (Django)

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/AtlantaFoodFinder.git
   cd AtlantaFoodFinder/backend
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

The backend API will be available at `http://localhost:8000`.

### Frontend (React)

1. Navigate to the React frontend directory:
   ```
   cd ../reactfoodfinder
   ```

2. Install the required npm packages:
   ```
   npm install
   ```

3. Start the React development server:
   ```
   npm start
   ```

The frontend application will be available at `http://localhost:3000`.

## Development Workflow

1. Run both the backend and frontend servers simultaneously.
2. Make API requests from the React frontend to `http://localhost:8000/api/...`.
3. Implement new features or fix bugs in the appropriate directories:
   - Backend changes: `backend/`
   - Frontend changes: `reactfoodfinder/src/`

## API Documentation

(Add information about your API endpoints, request/response formats, and authentication requirements here.)

## Environment Variables

### Backend

Create a `.env` file in the `backend/` directory with the following variables:
```
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=your_database_url
```

### Frontend

Create a `.env` file in the `reactfoodfinder/` directory with the following variables:
```
REACT_APP_API_URL=http://localhost:8000/api
```

## Testing

### Backend
```
cd backend
python manage.py test
```

### Frontend
```
cd reactfoodfinder
npm test
```

## Deployment

(Add instructions for deploying both the Django backend and React frontend to your preferred hosting platform.)

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes and commit them (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License.