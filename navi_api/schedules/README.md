# Navi API

Welcome to the Navi API project! This is a Django-based web application designed to provide a robust and scalable API for various functionalities.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with the Navi API, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/navi_api.git
    cd navi_api
    ```

2. **Set up the database**
    This project uses PostgreSQL for data storage.

    Open PGAdmin and configure you PostgreSQL database credentials. Navigate to the settings.py file in the navi_api > navi_api directory:
    Update the database settings with your own PostgreSQL credentials.

3. **Create a virtual environment:**
    ```bash
    python -m venv venv
        # On macOS/ Linux 
            `source venv/bin/activate` 
        # On Windows use 
            `venv\Scripts\activate`
    ```

4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    pip install django-cors-headers
    pip install djangorestframework
    pip install psycopg2  # or psycopg

    ```

5. **Set up the frontend**
    In a new terminal, navigate to the navi-web directory and install the required frontend dependencies:

    ```bash
    cd navi-web
    npm install
    ```
    
    Once the packages are installed, start the frontend development server:

    ```bash
    npm run dev
    ```

6. **Apply migrations:**
    Back in the terminal where the virtual environment is activated, apply the database migrations:

    ```bash
    cd navi_api
    python manage.py migrate
    ```
7. **Import data**
    python manage.py import_bus_schedules ..\\data\bus_schedules.csv
    python manage.py import_ferry_schedules .. \data\ferry_schedules.csv

8. **Run the development server:**
    Start the Django development server to begin interacting with the API:

    ```bash
    python manage.py runserver
    ```

## Usage

Once the server is running, you can access the API at `http://127.0.0.1:8000/`. Use tools like `curl` or Postman to interact with the endpoints.

## Features

- **User Authentication:** Secure user authentication and authorization. (Not implemented yet)
- **Data Management:** CRUD operations for managing data.
- **API Documentation:** Interactive API documentation using Swagger or similar tools.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
