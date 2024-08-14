import streamlit as st

def main():
    st.sidebar.title("Admin Panel")
    selection = st.sidebar.selectbox("Go to", ["Dashboard", "User Management", "Settings"])

    if selection == "Dashboard":
        from pages.dashboard import show_dashboard
        show_dashboard()
    elif selection == "User Management":
        from pages.users import manage_users
        manage_users()
    elif selection == "Settings":
        from pages.settings import show_settings
        show_settings()

if __name__ == "__main__":
    main()
