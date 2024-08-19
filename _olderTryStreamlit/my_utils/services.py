import streamlit as st


def dbAccess(func):
    def wrapper(*args, **kwargs):
        try:
            cursor = st.session_state.conn.cursor()
            if cursor:
                result = func(cursor, *args, **kwargs)
                st.session_state.conn.commit()
                cursor.close()
                return result
        except Exception as e:
            st.error(f"Failed to insert user into the database: {e}")
            return None
        return None

    return wrapper
