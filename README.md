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
    git clone https://github.com/wsmr9/order-management-service-interview.git
    cd order-management-service-interview
```

### Step 2: Set Up Environment Variables

Copy the `.env.example` file to create a `.env` file. This file will store all your environment-specific settings.

```bash
    cp .env.example .env
```

Open the `.env` file and make any necessary changes to fit your local development environment, but you can leave it as it is.

### Step 3: Create Required Directories


Create a directory within the root of the project to store PosgreSQL data:

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
- **Order Management Service**: The backend service for managing order data.

### Step 5: Initialize the Database


Once the Docker containers are running, you need to initialize the database:

1. Access phpMyAdmin at `http://localhost:5050`.
2. Log in using the credentials:
   - **Username:** admin@mail.com
   - **Password:** root
3. Open and Register an new conection:
    - In the window General, in the field name enter any name
    - In the window Connection:
        * Host name/addres field: postgres
        * Port field: 5432
        * Maintenance database: order_management
        * Username field: wayner
        * Password field: admin123
3. Navigate to the database "order_management" and go to Query Tool.
4. Open the `init-db.sql` file located in the root directory of your project and copy its contents.
5. Paste the SQL commands into the Query tab in PgAdmin and execute them to create the `orders` and `order_items` tables.


Verifying the Installation
--------------------------

To verify that your backend is set up correctly, navigate to the following URL, which will access the Order Management Service and display the orders:

```bash
    http://localhost:[PORT]/orders
```

Replace `[PORT]` with the port number you configured in your `.env` file.

**IF THE APPLICATION CONTAINER ORDERS ON PORT ESTABLISHED DID NOT RISE, PLEASE RUN THIS COMMAND AGAIN AND VERIFY**


```bash
    docker-compose up -d
```

THEN

```bash
    http://localhost:[PORT]/orders
```

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
