# Flask App Setup Guide

## Introduction

This document provides detailed instructions on how to set up and run the Flask application. Please follow the steps carefully to ensure the application runs correctly.

## Prerequisites

Before you start, ensure you have the following installed on your system:

- **Docker**: Needed to containerize the database, the Flask application, and other services.
- **Docker Compose**: Used to manage multi-container Docker applications.
- **Git**: Required for cloning the repository.

## Installation Steps

### Step 1: Clone the Repository

Clone the project repository and navigate into the directory:

```bash
    git clone [URL of the repository]
    cd [repository-name]
```

### Step 2: Set Up Environment Variables

Copy the `.env.example` file to create a `.env` file. This file will store all your environment-specific settings.

```bash
    cp .env.example .env
```

Open the `.env` file and make any necessary changes to fit your local development environment, but you can leave it as it is.

### Step 3: Create Required Directories


Create a directory within the root of the project to store MySQL data:

```bash
    mkdir postgres_data_order
```

### Step 4: Launch Docker Containers


Use Docker Compose to launch the services defined in your `docker-compose.yml`:

```bash
    docker-compose up -d
```

This command will start the following services:
- **Postgres Database**: Hosts the database for the application.
- **PgAmdin**: Provides a web interface for database management.
- **Order Management Service**: The backend service for managing product data.


Verifying the Installation
--------------------------

To verify that your backend is set up correctly, navigate to the following URL, which will access the Product Catalog Service and display the products:

```bash
    http://localhost:[PORT]/orders
```

Replace `[PORT]` with the port number you configured in your `.env` file.

Troubleshooting
---------------

If you encounter any problems, check the following:
- Ensure that all environment variables in the `.env` file are set correctly.
- Check the Docker container logs for any error messages:

```bash
    docker logs [container-name]
```

If issues persist, consider restarting the Docker containers or reinitializing the database.

Additional Help
---------------

For additional help or to report issues, please create an issue in the project's GitHub repository or contact the project maintainers directly.
