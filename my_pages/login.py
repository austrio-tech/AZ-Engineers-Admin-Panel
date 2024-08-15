import streamlit as st
import time
# Hardcoded credentials (username: admin, password: password)
USER_CREDENTIALS = {
    "admin": "password"
}

def login(username, password):
    """Check if the provided credentials are correct."""
    if USER_CREDENTIALS.get(username) == password:
        return True
    return False

def Login():
    st.title("Admin Panel")

    # Login Section
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(username, password):
            st.success("Login successful!")
            a = st.progress(0)
            for i in range(0, 101):
                a.progress(i)
            time.sleep(0.3)
            st.session_state.user = username
            st.session_state.page = "Dashboard"
            st.rerun()
            # Display the admin panel
        else:
            st.error("Invalid username or password")
