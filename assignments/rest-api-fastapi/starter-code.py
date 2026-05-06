# Building REST APIs with FastAPI

This assignment will guide you through creating a RESTful API using FastAPI.

## Getting Started

1. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

2. Create your main application file (e.g., `main.py`)

3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

## API Requirements

Your API should manage a simple resource. Choose one of:
- Todo items (tasks with title, description, completed status)
- User profiles (name, email, age)
- Book catalog (title, author, genre)

## Endpoints to Implement

- `GET /` - Welcome message
- `GET /items` - Get all items
- `GET /items/{id}` - Get specific item
- `POST /items` - Create new item
- `PUT /items/{id}` - Update item
- `DELETE /items/{id}` - Delete item

## Validation

Use Pydantic models to validate:
- Item creation requests
- Item update requests
- Path parameters (IDs)

## Testing

Test your API using:
- Browser for GET requests
- Tools like Postman or curl for other methods
- The automatic documentation at `http://localhost:8000/docs`