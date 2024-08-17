import streamlit as st

st.set_page_config(
    page_title="My Admin Panel",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
)
from my_utils.funcs import load_css
from my_utils.dbConn import create_connection
from my_pages.usersPage import manage_users
from my_pages.Awards import showImage
from my_pages.login import Login
from my_pages.settings import show_settings
from my_utils.openPage import OpenPage


def Urls():
    print(st.session_state, "session")
    print("query Params", st.query_params)
    if "p" in st.query_params:
        match st.query_params["p"]:
            case "users":
                if "user" in st.query_params:
                    OpenPage(manage_users, user=st.query_params.user, form="read")
                else:
                    OpenPage(manage_users)
            case "settings":
                OpenPage(show_settings)
            case "awards":
                OpenPage(showImage)
            case "login":
                OpenPage(Login)
            case _:
                st.error("Invalid page selected.")
    else:
        OpenPage()


def refreshPageOnUrl(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            Urls()
        except Exception as e:
            st.error(f"Some error occured: {e}")
        return None

    return wrapper


@refreshPageOnUrl
def GoTo(page=None, **kwargs):
    st.query_params.clear()
    if page:
        st.query_params["p"] = page
        for key, value in kwargs.items():
            st.query_params[key] = value


if "conn" not in st.session_state or st.session_state.conn is None:
    try:
        st.session_state.conn = create_connection()
    except Exception as e:
        st.error(f"An error occured while connecting with database: {e}")
if "user" not in st.session_state:
    GoTo("login")
else:
    if "p" not in st.query_params or st.query_params["p"] == "login":
        GoTo()
    if st.sidebar.button("Dashboard"):
        GoTo()
    if st.sidebar.button("User Management"):
        GoTo("users")
    if st.sidebar.button("Awards/Certificates"):
        GoTo("awards")
    if st.sidebar.button("Settings"):
        GoTo("settings")

load_css("styles/Home.css")
