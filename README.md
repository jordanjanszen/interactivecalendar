# Interactive Calendar

Interactive Calendar is a web application built with Django that helps users track their activities, nutrition, and sleep patterns. It allows users to log their daily activities, including workouts, meals, and sleep data, and provides insights into their overall fitness and wellness.

## Features

- **User Authentication**: Users can sign up for an account and log in securely to access their personalized calendar.
  
- **Activity Tracking**: Users can log their daily activities, including workouts, by providing details such as activity type, duration, distance, and calories burned.

- **Nutrition Logging**: The application allows users to track their nutritional intake by logging meals and snacks, specifying details such as fat, protein, carbohydrates, and total calories consumed.

- **Sleep Monitoring**: Users can record their sleep patterns, including bedtime, wake-up time, mood, and additional notes to track their sleep quality over time.

- **Calendar View**: The calendar view provides users with a visual representation of their activities, nutrition, and sleep data, allowing them to view and manage their daily entries.

## Getting Started

To run the application locally, follow these steps:

1. Clone the repository: `git clone https://github.com/jordanjanszen/interactivecalendar`
2. Navigate to the project directory: `cd interactivecalendar`
3. Install dependencies: `pip install -r requirements.txt`
4. Apply database migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`
6. Access the application in your web browser at `http://localhost:8000`

## Technologies Used

- **Django**: Web framework for building the backend of the application.
- **HTML/CSS/JavaScript**: Frontend technologies for creating user interfaces and interactivity.
- **Materialize CSS**: Frontend framework for styling and layout.
- **Postgresql**: Relational database management system used for storing user data.
- **Python**: Programming language used for backend development and scripting.

## Contributing

Contributions to the project are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a pull request.
