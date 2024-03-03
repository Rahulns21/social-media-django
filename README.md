# Social Media App using Django

This is a social media web application built using Django, where users can register, login, post updates, change passwords, and reset passwords if needed. Below is a brief overview of the features and how to set up the project.

## Features

- User Registration: Users can create an account by providing necessary details like username, email, and password.
- User Authentication: Registered users can log in securely using their credentials.
- Password Management: Users can change their passwords if needed.
- Password Reset: Forgot your password? No worries! Users can reset their passwords by following the password reset process.
- Post Creation: Users can create posts, share updates, and interact with other users' posts.
- User Profile: Each user has a profile where they can view their own posts and details.

## Technologies Used

- Django: A high-level Python web framework for rapid development.
- Django's Authentication System: Provides secure user authentication and management.
- Django Templates: For rendering HTML pages.
- SQLite: As the database for storing user information and posts.

## Installation

```bash
git clone https://github.com/your_username/social-media-app.git
cd social-media-app
python3 -m venv env
```

# On Windows:
.\env\Scripts\activate

# On macOS and Linux:
source env/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Usage

- Register a new account by clicking on the "Register" link and providing the required details.
- Log in using your registered credentials.
- Once logged in, you can create posts, view your profile, change your password, and reset your password if needed.
- Explore the application and interact with other users' posts.
