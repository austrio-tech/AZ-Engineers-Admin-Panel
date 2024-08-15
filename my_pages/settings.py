# # import streamlit as st

# # def show_settings():
# #     st.title("Settings")
# #     st.write("Change your application settings here.")

# #     new_value = st.text_input("Setting 1", "Default Value")
# #     if st.button("Save Settings"):
# #         st.write(f"Settings updated: {new_value}")

# import streamlit as st
# import mysql.connector
# from mysql.connector import Error
# from PIL import Image
# import io

# # MySQL connection setup
# def create_connection():
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host='your_host',
#             database='your_database',
#             user='your_username',
#             password='your_password'
#         )
#     except Error as e:
#         st.error(f"Error connecting to MySQL: {e}")
#     return connection
