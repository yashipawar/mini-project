1. github link : https://github.com/yashipawar/mini-project

2. How did you run the code: 
Here are the steps to run this Django project:
a) Clone the Repository:
````git clone <your-repo-url>`
`cd django-machine-test````

b) Set Up a Virtual Environment:
Create and activate a virtual environment:

````python -m venv venv`
`source venv/bin/activate  # On Linux/Mac`
`venv\Scripts\activate     # On Windows````

c) Install Dependencies:
Install all required dependencies from requirements.txt:

`pip install -r requirements.txt`

d) Configure Database:
Update settings.py with your MySQL/PostgreSQL database credentials:

`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Or 'django.db.backends.postgresql'
        'NAME': 'nimap_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '',  # Default MySQL port is 3306; PostgreSQL is 5432.
    }
}`

e) Apply Migrations:
Run migrations to create database tables:

`python manage.py makemigrations`
`python manage.py migrate`

f) Create a Superuser:
Create an admin user for accessing the Django admin panel:

`python manage.py createsuperuser`

g) Run the Development Server:
Start the Django development server:

`python manage.py runserver`

```Access the application at http://127.0.0.1:8000/.```

3. how did you run the machine test ?
The machine test involves testing several REST APIs for managing Users, Clients, and Projects.
a) Register a Client (POST /clients/)
Request:

`{
  "client_name": "Company A"
}`

Response:
`json
{
  "id": 1,
  "client_name": "Company A",
  "created_at": "2024-11-21T12:34:56Z",
  "created_by": "admin"
}`

b) Fetch Clients Info (GET /clients/)
Request: No body required.
Response:

`[
  {
    "id": 1,
    "client_name": "Company A",
    "created_at": "2024-11-21T12:34:56Z",
    "created_by": "admin"
  },
  {
    "id": 2,
    "client_name": "Company B",
    "created_at": "2024-11-21T12:40:00Z",
    "created_by": "admin"
  }
]`

c) Edit/Delete Client Info (PUT/PATCH/DELETE /clients/:id)
Update Client Info (PUT /clients/:id)
Request:

`{
  "client_name": "Updated Company A"
}`

Response:

`{
  "id": 1,
  "client_name": "Updated Company A",
  "created_at": "2024-11-21T12:34:56Z",
  "created_by": "admin",
  "updated_at": "2024-11-21T13:00:00Z"
}`

Delete Client Info (DELETE /clients/:id)
Response Status Code: 204 No Content.
d) Add New Projects for a Client (POST /projects/)
Request:

`{
  "project_name": "Project A",
  "client_id": 1,
  "users": [1, 2]
}`

Response:

`{
  "id": 1,
  "project_name": "Project A",
  "client": {
    "id": 1,
    "name": "Company A"
  },
  "users": [
    {"id": 1, "username": "user1"},
    {"id": 2, "username": "user2"}
  ],
  "created_at": "2024-11-21T13:30:00Z",
  "created_by": {"id": 1, "username": "admin"}
}`

e) Retrieve Assigned Projects for Logged-in Users (GET /projects/)
Response Example:

`[
    {
        "id": 1,
        "project_name": "Project A",
        "client_name": "Company A",
        "created_at": "2024-11-21T13:30:00Z",
        "created_by": {"id": 1, "username": "admin"}
    },
    {
        "id": 2,
        "project_name": "Project B",
        "client_name": "Company B",
        "created_at": "2024-11-21T14:00:00Z",
        "created_by": {"id": 1, "username": "admin"}
    }
]`

f) Delete a Project (DELETE /projects/:id)
Response Status Code: `204 No Content.`

4. DB Design :
User: Use Django's default User model.
a) Client:
id: Auto-generated primary key.
client_name: Name of the client.
created_by: Foreign key to the User model (the user who created the client).
created_at: Timestamp when the client was created.
updated_at: Timestamp when the client was last updated.

v) Project:
id: Auto-generated primary key.
project_name: Name of the project.
client: Foreign key to the Client model (the client associated with the project).
users: Many-to-Many relationship with the User model (users assigned to this project).
created_by: Foreign key to the User model (the user who created the project).
created_at: Timestamp when the project was created.
