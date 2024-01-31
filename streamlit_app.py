# api_key = "AIzaSyDMp36mRwTWPHm0LnSkVcSOt3zd-WJWuQk"
import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key="AIzaSyDMp36mRwTWPHm0LnSkVcSOt3zd-WJWuQk")


def get_gemini_response(input_prompt, input_image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_prompt, input_image[0]])
    return response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_part = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_part
    else:
        raise FileNotFoundError("No File Uploaded")


st.set_page_config(page_title="Calories Advisor App")

st.header("Calories Advisor App")
uploaded_file = st.file_uploader(
    "choose an image", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about total calories")

input_prompt = """
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----
            Finally you can also mentaion wheather the food is healthy or not and also mentaion the
            percentage split of the ratio of carbohydrates, fats, fibers,sugar, protien and other important thing required in the diet.


"""

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data)
    st.subheader("Response")
    st.write(response)
