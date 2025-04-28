# DJ01

A simple Django website with responsive design using Bootstrap 5.

## Description

DJ01 is a demonstration Django project showing the implementation of a multi-page website with a common design for the header and footer. The project includes:
- Responsive design based on Bootstrap 5
- Dynamic menu with highlighting of the active page
- Reusable templates thanks to the Django template engine
- Organized structure with a separate "main" application

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/dj01.git
cd dj01
```

2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run migrations:
```
python manage.py migrate
```

5. Start the development server:
```
python manage.py runserver
```

6. Open http://127.0.0.1:8000/ in your browser

## Project Structure

```
DJ01/
├── DJ01/                 # Main Django project
│   ├── __init__.py
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL routing
│   ├── asgi.py
│   └── wsgi.py
├── main/                 # "main" application
│   └── migrations        # Migration files not used yet.
│   └── static/           # Static files (CSS, JS, images)
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
├   └── templates/        # HTML templates
│   │   └── main          # main templates
│   │       ├── base.html     # Base template
│   │       ├── index.html    # Home page
│   │       ├── about.html    # About us
│   │       ├── services.html # Services
│   │       ├── blog.html     # Blog
│   │       └── contacts.html # Contacts
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py           # App URLs
│   └── views.py          # Views
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

## Features

- **Home Page**: Overview of main features with content blocks
- **About Us**: Information about the company and team
- **Services**: List of provided services with icons
- **Blog**: List of blog posts with images and short descriptions
- **Contacts**: Contact information and feedback form

## Technologies

- Django 4.2+
- Bootstrap 5
- Bootstrap Icons
- HTML5 / CSS3

## Future Development

- Adding a database to store content information
- Developing an admin panel for content management
- Integration with user authentication system
- Adding API for mobile applications

## Author

[Ivan Vorobev] - [ivan.vorobjov(at)gmail.com]

## License

This project is distributed under the MIT license. See the LICENSE file for details.