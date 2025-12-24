# Project Week 10 - Contacts API

## Project Description
This project is a simple Contacts API built using FastAPI and MySQL. The project consists of two Docker containers: one for the MySQL database and one for the FastAPI application. The API supports full CRUD operations (Create, Read, Update, Delete) for managing contacts.

### API Endpoints
- **GET /contacts**: Retrieve all contacts
- **POST /contacts**: Create a new contact
- **PUT /contacts/{id}**: Update an existing contact by ID
- **DELETE /contacts/{id}**: Delete a contact by ID

## Project Structure
```
project-week-10/
├── app/
│   ├── main.py            # FastAPI application
│   ├── data_interactor.py # Database interaction logic
│   ├── Dockerfile         # Dockerfile for API container
│   └── requirements.txt   # Python dependencies
├── sql/
│   └── init.sql           # SQL initialization script
├── .env                   # Environment variables for Docker
├── compose.yaml           # Docker Compose configuration
├── .gitignore             # Ignored files
└── README.md              # Project documentation
```

## Setup Instructions

1. Make sure Docker is installed on your system.
2. Navigate to the project root directory.
3. Build and run the containers using Docker Compose:
```bash
docker compose up -d
```
This command will create and start two containers:
- **mysql_db**: MySQL 8.0 database
- **api**: FastAPI application

The MySQL container runs with the database initialized from `init.sql`. The API container waits until the database is healthy before starting.

## Testing Instructions

You can test the API endpoints using `curl` commands or any API client like Postman.

### Get all contacts
```bash
curl http://localhost:8000/contacts
```

### Create a new contact
```bash
curl -X POST http://localhost:8000/contacts \
-H "Content-Type: application/json" \
-d '{"first_name": "Alice", "last_name": "Brown", "phone_number": "050-1234567"}'
```

### Update a contact
```bash
curl -X PUT http://localhost:8000/contacts/1 \
-H "Content-Type: application/json" \
-d '{"phone_number": "052-7654321"}'
```

### Delete a contact
```bash
curl -X DELETE http://localhost:8000/contacts/1
```

## Notes
- The API connects to the database using environment variables defined in the `compose.yaml` file.
- Docker Compose ensures that the API container only starts when the MySQL database is ready.
- All Python dependencies are defined in `requirements.txt` and installed in the API container.
- Use the `docker ps` command to check the status of running containers and `docker logs <container_name>` for debugging.

