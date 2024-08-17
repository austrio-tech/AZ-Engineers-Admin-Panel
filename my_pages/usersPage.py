import streamlit as st
from my_utils.users import *
import pandas as pd
def manage_users():
    st.title("User Management")
    st.write("Manage the users of your platform.")

    # if st.button("Add User"):
    #     st.session_state.form = "Add-User"
    #     st.rerun()
    # Create a row of buttons using columns

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Add User"):
            st.session_state.form = "Add-User"
            st.rerun()

    # with col2:
    #     if st.button("Update User"):
    #         st.session_state.form = "Update-User"
    #         st.rerun()

    with col3:
        if st.button("Read User"):
            st.session_state.form = "Read-User"
            st.rerun()

    with col4:
        if st.button("Read all Users"):
            st.session_state.form = "Read-All-User"
            st.rerun()
    if "form" not in st.session_state:
        ...
    elif st.session_state.form == "Add-User":
        with st.form("add_user"):
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            role = st.selectbox("Role", ["Admin", "User"])
            profilePic = st.file_uploader("Profile Picture", type=["png", "jpg", "jpeg"], accept_multiple_files=False, help="Max size: 65KB")
            if profilePic is not None and profilePic.size > 65000:
                st.error("Profile picture size should not exceed 65KB.")
                return
            submitted = st.form_submit_button("Add User")
            if submitted:
                if first_name and last_name and email and password:
                    user = User(first_name, last_name, email, password, role, profilePic)
                    cid = CreateUser(user)
                    if cid:
                        st.success("User added successfully.")
                    else:
                        st.error("Error adding user.")
                else:
                    st.error("Please fill all the fields.")

    elif st.session_state.form == "Update-User":
        st.write("Remove user functionality goes here.")

    elif st.session_state.form == "Read-User":
        user_id = st.text_input("Enter user ID:")
        if user_id:
            user_id = int(user_id)
            user = ReadUser(user_id)
            if user:
                st.write(f"User ID: {user.id}")
                st.write(f"First Name: {user.first_name}")
                st.write(f"Last Name: {user.last_name}")
                st.write(f"Email: {user.email}")
                st.write(f"Role: {user.role}")
                st.write(f"Last Edit: {user.last_edit}")
                st.write(f"Status: {'Active' if user.status else 'Inactive'}")
                if user.profilePic:
                    st.image(user.profilePic)
            else:
                st.error("User not found.")

    elif st.session_state.form == "Read-All-User":
        users = ReadAllUsers()
        if users:
            df = pd.DataFrame([user.__dict__ for user in users])
            df = df[['id',"first_name", "last_name", "email", "role", "last_edit", "status"]]
            # st.dataframe(df, hide_index=True)
            st.markdown("### Users List")
            table_md = "| ID | First Name | Last Name | Email | Role | Last Edit | Status | Action |\n"
            table_md += "|---|------------|-----------|-------|------|-----------|--------|--------|\n"
            for _, row in df.iterrows():
                edit_link = f"[Edit](http://localhost:8501/?edit_user_id={row['id']})"
                table_md += f"| {row['id']} | {row['first_name']} | {row['last_name']} | {row['email']} | {row['role']} | {row['last_edit']} | {row['status']} | {edit_link} |\n"

            st.markdown(table_md, unsafe_allow_html=True)
            query_params = st.query_params
            if 'edit_user_id' in query_params:
                user_id = int(query_params['edit_user_id'])
                st.write(f"Editing user with ID: {user_id}")

    
