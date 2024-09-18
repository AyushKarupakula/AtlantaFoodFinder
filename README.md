# AtlantaFoodFinder

AtlantaFoodFinder is a Django-based web application that helps users discover and explore restaurants in Atlanta, Georgia.

## Features

- Browse restaurants by cuisine type
- Search for restaurants by name or location
- View restaurant details, including menu, hours, and reviews
- User authentication and profile management
- Add and manage favorite restaurants

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/AtlantaFoodFinder.git
   cd AtlantaFoodFinder
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

7. Open your browser and navigate to `http://localhost:8000`

## Project Structure

- `atlantafoodfinder/`: Main Django project directory
- `restaurants/`: Django app for restaurant-related functionality
- `users/`: Django app for user authentication and profiles
- `templates/`: HTML templates
- `static/`: Static files (CSS, JavaScript, images)

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes and commit them (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License.