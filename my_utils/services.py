import streamlit as st

def dbAccess(func):
    def wrapper(*args, **kwargs):
        cursor = st.session_state.conn.cursor()
        if cursor:
            result = func(cursor, *args, **kwargs)
            cursor.close()
            return result
        return None
    return wrapper