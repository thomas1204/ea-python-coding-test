import os
import psycopg2.extras
from psycopg2 import pool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "my_database")
DB_USER = os.getenv("DB_USER", "my_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "my_password")

# Create a global connection pool
connection_pool = None


def init_connection_pool():
    """Initialize a connection pool"""
    global connection_pool
    if connection_pool is None:
        try:
            connection_pool = pool.SimpleConnectionPool(
                1,
                20,  # min 1 connection, max 20 connections
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port="5432",
                database=DB_NAME,
                cursor_factory=psycopg2.extras.RealDictCursor,
            )
            if connection_pool:
                print("Connection pool created successfully.")
        except Exception as e:
            print(f"Error creating connection pool: {e}")
            raise e


def get_connection():
    """Fetch a connection from the pool"""
    global connection_pool
    if connection_pool is None:
        init_connection_pool()

    try:
        connection = connection_pool.getconn()
        if connection:
            print("Successfully retrieved connection from pool.")
        return connection
    except Exception as e:
        print(f"Error getting connection: {e}")
        raise e


def release_connection(conn):
    """Release the connection back to the pool"""
    global connection_pool
    if connection_pool:
        connection_pool.putconn(conn)
        print("Connection returned to pool.")


def close_all_connections():
    """Close all connections in the pool"""
    global connection_pool
    if connection_pool:
        connection_pool.closeall()
        print("All connections in the pool have been closed.")
