import streamlit as st
from gtts import gTTS
import tempfile
import os
from PIL import Image
from io import BytesIO

# Define the Streamlit app
def main():
    # Set page configuration
    st.set_page_config(page_title="VocaGenie", layout="wide")

    # Custom CSS for multi-color backgrounds
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(45deg, #00FFFF, #00FFFF, #008B8B, #FF1493, #FFC0CB, #A020F0, #D0E1F9);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        @keyframes gradient {
            0% { background-position: 0% 0%; }
            50% { background-position: 100% 100%; }
            100% { background-position: 0% 0%; }
        }
        .css-1d391kg {
            background: linear-gradient(135deg, #ff6f61, #d4a5a5);
        }
        .css-14y4q6d {
            background: linear-gradient(135deg, #ff6f61, #d4a5a5);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Sidebar
    with st.sidebar:
        imgURL = 'https://raw.githubusercontent.com/Areesa110/VocaGenie/main/Text-To-SpeechImage.PNG'
        st.image(imgURL, caption='')  # Placeholder image
        st.title('VocaGenie')
        st.write("### Description")
        st.write(
            """
            Convert your text into speech with this simple tool. Input text and generate an audio file 
            that you can play or download. This app uses Google Text-to-Speech (gTTS) to perform the conversion.
            """
        )
        st.write("### Features")
        st.write(
            """
            - Convert text into speech with natural-sounding voices.
            - Download the generated audio file.
            - User-Friendly Interface.
            """
        )

    # Main Layout
    st.title('Welcome to VocaGenie')
    st.write("### How to Use")
    st.write(
        """
        1. Enter the text you want to convert into speech in the text area below.
        2. Click on the 'Generate Speech' button to convert the text.
        3. Listen to the generated speech or download the audio file.
        """
    )

    # User Input
    user_input = st.text_area("Enter your text here")

    # Button to generate speech
    if st.button("Generate Speech"):
        if user_input:
            # Generate speech
            tts = gTTS(text=user_input, lang='en')
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
                tts.save(temp_file.name)
                temp_file.seek(0)
                st.audio(temp_file.name, format='audio/mp3')
                st.download_button(
                    label="Download Audio",
                    data=temp_file.read(),
                    file_name="output.mp3",
                    mime="audio/mp3",
                )
        else:
            st.error("Please enter some text to convert.")

if __name__ == "__main__":
    main()
