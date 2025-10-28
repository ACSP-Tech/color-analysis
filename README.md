## Bincom Staff Assessment: Color Analysis and Algorithms API

This project provides a comprehensive solution to the Bincom Staff Assessment, implemented as a high-performance, asynchronous REST API using FastAPI and SQLModel (for PostgreSQL integration).

The application performs data analysis on staff dress colors extracted from an HTML source and provides endpoints for complex algorithms.

#### Key Features (Assessment Questions Solved)

The API is structured to answer the nine assessment questions:

Mean Color: Calculates the mode (most frequent) color (Categorical data mean).

Mostly Worn Color: Identifies the color worn most frequently throughout the week.

Median Color: Finds the middle color in the alphabetically sorted list of all worn colors.

BONUS: Color Variance: Calculates the variance of the color frequencies.

BONUS: Probability (Red): Determines the probability of choosing Red randomly.

Database Storage: Inserts color frequencies into a PostgreSQL database (Simulated/Real, depending on configuration).

BONUS: Recursive Search: Implements a Recursive Binary Search algorithm.

Binary to Base 10: Generates a random 4-digit binary number and converts it to its base 10 equivalent.

Fibonacci Sum: Calculates the sum of the first 50 Fibonacci numbers.

###  Setup and Installation

Prerequisites

You must have Python 3.10+ installed.

Dependencies

the core packages required are:

pip install fastapi uvicorn[standard] sqlmodel asyncpg pydantic


For the exact environment reproduction, here is the detailed list:

annotated-doc==0.0.3
annotated-types==0.7.0
anyio==4.11.0
asyncpg==0.30.0
click==8.3.0
colorama==0.4.6
fastapi==0.120.1
greenlet==3.2.4
h11==0.16.0
idna==3.11
pydantic==2.12.3
pydantic_core==2.41.4
python-decouple==3.8
sniffio==1.3.1
SQLAlchemy==2.0.44
sqlmodel==0.0.27
starlette==0.48.0
typing-inspection==0.4.2
typing_extensions==4.15.0
uvicorn==0.38.0


### Database Configuration (PostgreSQL/Supabase)

The application requires a PostgreSQL database connection (e.g., via Supabase). You must set your database connection URL as an environment variable or in a .env file (python-decouple is listed in your dependencies, suggesting environment file usage).

Format for async connections (using Supabase Transaction Pooler):

DATABASE_URL="postgresql+asyncpg://user:password@host:6543/dbname"


Note: The application uses connect_args={"statement_cache_size": 0} to handle compatibility with connection poolers like Pgbouncer.

🏃 How to Run the Application

Navigate to your project's root directory:

cd Colour\ Analysis\color-analysis-bincom


Start the Uvicorn server, targeting the app.main module (assuming your main application instance is named app):

uvicorn app.main:app --reload


The API will be available at [color-analysis](https://color-analysis-bincom-assess.up.railway.app).
