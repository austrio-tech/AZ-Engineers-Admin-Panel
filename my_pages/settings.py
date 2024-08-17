import streamlit as st


def show_settings():
    st.title("Settings")
    st.write("Change your application settings here.")

    new_value = st.text_input("Setting 1", "Default Value")
    if st.button("Save Settings"):
        st.write(f"Settings updated: {new_value}")
