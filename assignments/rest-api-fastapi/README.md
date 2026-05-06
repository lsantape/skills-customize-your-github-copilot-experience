# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a RESTful API using FastAPI that manages a simple resource (like a todo list or user database). You'll learn about HTTP methods, request/response handling, and API design principles.

## 📝 Tasks

### 🛠️ Set Up the FastAPI Application

#### Description
Initialize a FastAPI application with basic structure and dependencies.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn
- Create a main FastAPI app instance
- Set up a basic root endpoint that returns a welcome message
- Run the server locally

### 🛠️ Implement CRUD Operations

#### Description
Add endpoints for Create, Read, Update, and Delete operations on your chosen resource.

#### Requirements
Completed program should:

- Implement GET endpoint to retrieve all items
- Implement POST endpoint to create new items
- Implement PUT/PATCH endpoint to update existing items
- Implement DELETE endpoint to remove items
- Use appropriate HTTP status codes
- Handle basic error cases (e.g., item not found)

### 🛠️ Add Data Validation and Documentation

#### Description
Enhance the API with input validation and automatic documentation.

#### Requirements
Completed program should:

- Use Pydantic models for request/response validation
- Add path parameters and query parameters where appropriate
- Include meaningful error messages
- Generate and view the interactive API documentation