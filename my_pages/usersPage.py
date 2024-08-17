import streamlit as st
from my_utils.openPage import OpenPage


def manage_users(user=None, form=None):
    st.title("User Management")
    st.write("Manage the users of your platform.")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Add User"):
            form = "add"

    with col2:
        if st.button("Update User"):
            form = "update"

    with col3:
        if st.button("Read User"):
            form = "read"

    with col4:
        if st.button("Read all Users"):
            form = "readAll"

    if form:
        st.session_state["form"] = form
    OpenPage(user_menu, user=user, form=form)


import pandas as pd

# from my_utils.goTo import GoTo
from my_utils.users import CreateUser, ReadUser, ReadAllUsers

# def editUser(id):
#     print(id, 'id')
#     GoTo('users', user=id)


def user_menu(user=None, form=None):
    print(user, form)
    if not form:
        print()
        if "form" in st.session_state:
            form = st.session_state.form

    if form == "add":
        with st.form("add_user"):
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            role = st.selectbox("Role", ["Admin", "User"])
            profilePic = st.file_uploader(
                "Profile Picture",
                type=["png", "jpg", "jpeg"],
                accept_multiple_files=False,
                help="Max size: 65KB",
            )
            if profilePic is not None and profilePic.size > 65000:
                st.error("Profile picture size should not exceed 65KB.")
                return
            submitted = st.form_submit_button("Add User")
            if submitted:
                if first_name and last_name and email and password:
                    user = User(
                        first_name, last_name, email, password, role, profilePic
                    )
                    cid = CreateUser(user)
                    if cid:
                        st.success("User added successfully.")
                    else:
                        st.error("Error adding user.")
                else:
                    st.error("Please fill all the fields.")

    elif form == "update":
        st.write("Remove user functionality goes here.")

    elif form == "read":
        user_id = st.text_input("Enter user ID:", key="readUser")
        if user:
            User = ReadUser(user)
            if User:
                st.write(f"User ID: {User.id}")
                st.write(f"First Name: {User.first_name}")
                st.write(f"Last Name: {User.last_name}")
                st.write(f"Email: {User.email}")
                st.write(f"Role: {User.role}")
                st.write(f"Last Edit: {User.last_edit}")
                st.write(f"Status: {'Active' if User.status else 'Inactive'}")
                if User.profilePic:
                    st.image(User.profilePic)
            else:
                st.error("User not found.")
        if user_id:
            # editUser(user_id)
            user_id = int(user_id)
            st.query_params["user"] = user_id
            # ag = {'user': user_id}
            # print(ag, "ag")
            # GoTo("users", form='read', **ag)

    elif form == "readAll":
        users = ReadAllUsers()
        print("reading all users")
        if users:
            df = pd.DataFrame([user.__dict__ for user in users])
            df = df[
                [
                    "id",
                    "first_name",
                    "last_name",
                    "email",
                    "role",
                    "last_edit",
                    "status",
                ]
            ]
            st.dataframe(df, hide_index=True)
        else:
            st.error("No users found.")
