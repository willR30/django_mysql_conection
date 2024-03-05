# Django and MySQL Database conection

This project is a Django-based web application that utilizes a MySQL database for data storage. It follows best practices by configuring the database connection parameters and sensitive information such as database credentials using environment variables.

## Project Components

### Django

The project is built using the Django web framework, which provides a robust structure for developing web applications in Python. Django offers features such as ORM (Object-Relational Mapping) for database interactions, a built-in admin interface, and a powerful templating engine.

### MySQL Database

For data storage, the project utilizes a MySQL database. MySQL is a popular relational database management system known for its performance, reliability, and scalability.

### Environment Variables

Sensitive information like database credentials and server connection details are stored as environment variables. This practice enhances security by keeping sensitive data out of version control and configuration files.

## Configuration

### Exporting Environment Variables

To set up the project environment, export the following environment variables:

- `DB_NAME`: Name of the MySQL database.
- `DB_USER`: Username for MySQL database access.
- `DB_PASSWORD`: Password for MySQL database access.
- `DB_HOST`: Hostname or IP address of the MySQL database server.
- `DB_PORT`: Port number for connecting to the MySQL database server.
- `SERVER_HOST`: Hostname or IP address where the Django server should listen.
- `SERVER_PORT`: Port number where the Django server should listen.

Replace the placeholder values with the actual credentials and server details.

### Django Settings

In the Django project's `settings.py` file, access the environment variables to configure the database connection and server settings. Here's an example:

```python
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'default_db_name'),
        'USER': os.environ.get('DB_USER', 'default_db_user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'default_db_password'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '3306'),
    }
}

SERVER_HOST = os.environ.get('SERVER_HOST', 'localhost')
SERVER_PORT = os.environ.get('SERVER_PORT', '8000')
