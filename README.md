# posts-management-app

This project is a system built with FastAPI for the backend and React with Vite for the frontend. It allows users to register, log in, and manage posts.

## Backend

The backend is built with FastAPI and SQLAlchemy.

### Setup

1. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\Activate.ps1`
    ```

2. Install the dependencies:
    ```sh
    pip install fastapi sqlalchemy pymysql passlib
    ```

3. Run the FastAPI server:
    ```sh
    uvicorn main:app --reload
    ```

### Database Configuration

The database configuration is located in [database.py]. Update the [DATABASE_URL] with your database credentials.

### Routes

- User routes are defined in [user.py].
- Post routes are defined in [post.py].

## Frontend

The frontend is built with React and Vite.

### Setup

1. Navigate to the [front-end] directory:
    ```sh
    cd front-end
    ```

2. Install the dependencies:
    ```sh
    npm install
    ```

3. Run the development server:
    ```sh
    npm run dev
    ```

### Pages

- The main entry point is src/main.jsx.
- The main application component is src/App.jsx.
- The registration page is src/pages/register.jsx.
- The login page is src/pages/Login.jsx.
- The home page is src/pages/Home.jsx.

