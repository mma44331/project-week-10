# Contacts API Project

## Project Description
This project is a simple Contacts API built using FastAPI and MySQL. It provides CRUD operations for managing contacts.

**API Endpoints:**

| Method | Endpoint            | Description                       |
|--------|--------------------|-----------------------------------|
| GET    | /contacts          | Retrieve all contacts             |
| POST   | /contacts          | Create a new contact              |
| PUT    | /contacts/{id}     | Update an existing contact        |
| DELETE | /contacts/{id}     | Delete a contact                  |

## Setup Instructions

1. Make sure Docker and Docker Compose are installed on your machine.
2. Clone the project repository.
3. Navigate to the project root directory.
4. Create a `.env` file with the following content:

```env
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=contacts_db
```

5. Run the project using Docker Compose:

```bash
docker compose up -d
```

This will start:
- **MySQL container (`mysql_db`)** with database initialized from `init.sql`.
- **API container (`api`)** connected to the MySQL database.

The API will be available at `http://localhost:8000`.

## Testing Instructions

You can test the API endpoints using `curl` or any API client like Postman.

**Get all contacts:**
```bash
curl http://localhost:8000/contacts
```

**Create a new contact:**
```bash
curl -X POST http://localhost:8000/contacts \
-H "Content-Type: application/json" \
-d '{"first_name":"Alice","last_name":"Wonder","phone_number":"050-1234567"}'
```

**Update a contact:**
```bash
curl -X PUT http://localhost:8000/contacts/1 \
-H "Content-Type: application/json" \
-d '{"phone_number":"052-7654321"}'
```

**Delete a contact:**
```bash
curl -X DELETE http://localhost:8000/contacts/1
```

## Project Structure
```
project-week-10/
├── app/
│   ├── main.py
│   ├── Dockerfile
│   ├── data_interactor.py
│   └── requirements.txt
├── sql/
│   └── init.sql
├── .env
├── compose.yaml
├── .gitignore
└── .venv/
```

## Notes
- The MySQL container initializes the database using `init.sql`.
- The API waits until the MySQL service is healthy before starting.
- Environment variables are used to configure the database connection.
- Error handling is included in all database operations.

