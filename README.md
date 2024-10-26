# Todo App

A simple Todo application built using HTML, Bootstrap, and Django. This app allows users to create, manage, and track tasks easily.

## Features

- **Add Tasks**: Quickly add new tasks to your to-do list.
- **Mark as Complete**: Easily mark tasks as completed.
- **View Completed Tasks**: Check the list of completed tasks with timestamps.
- **Delete Tasks**: Remove tasks from your list.
- **Responsive Design**: The app is fully responsive and works on various devices.

## Technologies Used

- **Frontend**: HTML, Bootstrap, Font Awesome
- **Backend**: Django
- **Database**: SQLite (or any preferred database)

## Installation

### Prerequisites

- Python 3.x
- Django

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/todo-app.git
   cd todo-app
   ```

2. **Install Dependencies**:

   Create a virtual environment and install Django:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install django
   ```

3. **Run Migrations**:

   ```bash
   python manage.py migrate
   ```

4. **Start the Development Server**:

   ```bash
   python manage.py runserver
   ```

5. **Access the App**:

   Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

- Use the input field to add new tasks.
- Click "Mark as Done" to complete a task.
- Use the "Mark as Not Done" button to revert a completed task.
- Delete tasks using the trash icon.
