import streamlit as st
from my_utils.ImgCtrt import fetch_image

from PIL import Image
import io

def showImage():
    st.title("View Award Image")

    award_id = st.number_input("Enter Award ID", min_value=1, step=1)
    if st.button("Fetch Image"):
        print("button pressed")
        st.write("button pressed...")
        record = fetch_image(award_id)
        try:
            st.write(f"Award ID entered: {award_id}")
            if record:
                title, img_data = record
                st.write(f"Title: {title}")
                image = Image.open(io.BytesIO(img_data))
                st.image(image, caption=title)
            else:
                st.error("No record found with this ID.")
        except Exception as e:
            st.write(f"Error occurred: {e}")
