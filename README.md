# FastAPI-social-media-app

A social media web application built with FastAPI and PostgreSQL. This project is intended to demonstrate how to build a backend API using modern technologies.

## Features

- It allows to create, delete and update a post
- It retrieves all of the available posts or just one by using an ID
- User registration
- Schemas implemented to validate input and output data
- Users cannot update nor delete posts that do not own
- Users can vote posts: Add and delete votes to a post
- User authentication and authorization using JWT tokens.

Language: Python v3.10.8

## Tech stack

1. Backend: FastAPI v0.115.0 FastAPI - Python web framework.
2. Alembic: v1.13.3
3. Database: PostgreSQL v15.2
4. Models: SQLAlchemy v2.0.35
5. Security:
    - JWT and OAuth2 implementation
    - Hashed passwords in database using passlib v1.7.4
    - Deploy:
        - Deploy to an Ubuntu server on AWS