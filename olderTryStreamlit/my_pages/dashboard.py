import streamlit as st
from my_utils.funcs import *

load_css("styles/dashboard.css")


def show_dashboard():
    st.title("Dashboard")
    st.write("This is the admin dashboard.")

    st.metric("Total Users", "1024")
    st.metric("Active Sessions", "342")
    st.metric("Server Uptime", "99.99%")
