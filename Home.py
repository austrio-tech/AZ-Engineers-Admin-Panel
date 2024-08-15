import streamlit as st
from my_pages.dashboard import show_dashboard
from my_pages.users import manage_users
from my_pages.Awards import showImage
from my_pages.login import Login
# from my_pages.settings import show_settings
from my_utils.funcs import load_css
from my_utils.dbConn import create_connection
# Configure the page
# st.set_page_config(
#     page_title="My Admin Panel",
#     page_icon="👨‍💻",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# Load custom CSS
if "conn" not in st.session_state or st.session_state.conn is None:
    st.session_state.conn = create_connection()
if "user" not in st.session_state:
    st.session_state.page = "login"
else:
    if 'page' not in st.session_state:
        st.session_state.page = 'Dashboard'

    # Sidebar navigation using buttons
    st.sidebar.title("Admin Panel")
    if st.sidebar.button("Dashboard"):
        st.session_state.page = 'Dashboard'
    if st.sidebar.button("User Management"):
        st.session_state.page = 'User Management'
    if st.sidebar.button("Awards/Certificates"):
        st.session_state.page = 'Awards/Certificates'
    if st.sidebar.button("Settings"):
        st.session_state.page = 'Settings'

match st.session_state.page:
    case 'Dashboard':
        show_dashboard()
    case 'User Management':
        manage_users()
    case 'Awards/Certificates':
        showImage()
    case 'login':
        Login()
    case _:
        st.error("Invalid page selected.")

load_css("styles/Home.css")