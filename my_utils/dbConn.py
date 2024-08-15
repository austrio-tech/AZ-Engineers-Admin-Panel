import mysql.connector
from mysql.connector import Error
import streamlit as st

# MySQL connection setup
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='az-database',
            user='root',
            password=''
        )
        print(connection, "successful")
    except Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        print(f"Error connecting to MySQL: {e}")
    return connection