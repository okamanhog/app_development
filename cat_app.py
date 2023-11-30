import streamlit as st
import requests

# code to configure the streamlit page
st.set_page_config(
    page_title="Cat Aoo",
    page_icon=":cat:"
)

st.header("welcome to my cat app :)", divider="rainbow")
#####

#request cat image from API
def get_content():
    contents = requests.get("https://cataas.com//cat")
    return contents.content

#place requested cat image on streamlit app
def place_cat_image():
    cat_image = get_content()
    st.image(cat_image, width=200)


#
st.button("Click Here",
          on_click =place_cat_image)
