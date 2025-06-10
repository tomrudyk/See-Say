import streamlit as st
from PIL import Image
import os
from singleLLM import run_LLM_model_evaluation_fullInference


# Set the page title
st.set_page_config(page_title="Image and Audio Viewer", layout="centered")

st.title("Hello!")
st.write("Displaying your image. \nThe audio file will attempt to play automatically.")

# Input for image path
image_path_default = "img1.png" # Set the default image path
image_path = st.text_input("Image File Path", image_path_default)
audio_path = "q1_whyHappy.mp3"
audio_path_childAnswer = "a1_gotIceCream.mp3"

image_displayed_successfully = False

# --- Image Display Section ---
st.markdown("---")
st.subheader("🖼️ Image Display")

if image_path:
    if os.path.exists(image_path):
        try:
            image = Image.open(image_path)
            st.image(image, caption=f"Image from: {image_path}")
            image_displayed_successfully = True
        except Exception as e:
            st.error(f"**Error loading image:** {e}")
            st.warning("Please ensure the **image path** is correct and the file is a valid image format (e.g., .png, .jpg, .jpeg, .gif, .bmp).")
    else:
        st.warning(f"**Image file not found:** `{image_path}`")
        st.info("Please make sure the image file exists at the specified path.")
else:
    st.info("Please enter an image file path to display the image.")





# --- Audio Playback Section ---
st.markdown("---")
st.subheader("🔊 Leading Question")

if image_displayed_successfully:
    if os.path.exists(audio_path):
        try:
            audio_file = open(audio_path, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3', start_time=0) # start_time=0 helps ensure it attempts to play from the beginning
            st.info("*(Note: Modern browsers may block automatic audio playback until a user interacts with the page. You might need to click the play button.)*")
        except Exception as e:
            st.error(f"**Error loading or playing audio:** {e}")
            st.warning("Please ensure the **audio path** is correct and the file is a valid audio format (e.g., .mp3, .wav, .ogg).")
    else:
        st.warning(f"**Audio file not found:** `{audio_path}`")
        st.info(f"Please make sure the audio file '{audio_path}' exists in the same directory as the script.")
else:
    st.info("Audio will attempt to play once the image is successfully loaded and displayed.")


st.markdown("---")
st.subheader("🔊 Child Answer")

if image_displayed_successfully:
    if os.path.exists(audio_path_childAnswer):
        try:
            audio_file = open(audio_path_childAnswer, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3', start_time=0) # start_time=0 helps ensure it attempts to play from the beginning
        except Exception as e:
            st.error(f"**Error loading or playing audio:** {e}")
            st.warning("Please ensure the **audio path** is correct and the file is a valid audio format (e.g., .mp3, .wav, .ogg).")
    else:
        st.warning(f"**Audio file not found:** `{audio_path_childAnswer}`")
        st.info(f"Please make sure the audio file '{audio_path_childAnswer}' exists in the same directory as the script.")
else:
    st.info("Audio will attempt to play once the image is successfully loaded and displayed.")


import subprocess

st.markdown("---")
st.subheader("🧠 Run Inference")

if st.button("Run Inference and Play Output"):
    st.info("Running inference... please wait.")

    try:
        # Run the inference script
        result = subprocess.run(["python", "inference.py"], capture_output=True, text=True)

        if result.returncode == 0:
            if True:

                st.success("Inference completed successfully.")
                st.subheader("🔊 Model Output: ")
                output_audio_path = "output_audio.mp3"
                outputLLM_path = "outputLLM.txt"


                if os.path.exists(output_audio_path):
                    try:
                        with open(output_audio_path, 'rb') as audio_file:
                            audio_bytes = audio_file.read()
                            st.audio(audio_bytes, format='audio/mp3', start_time=0)
                            st.success("Output audio generated and played.")
                        with open(outputLLM_path, 'r') as file:
                            output_text = file.read()
                            st.markdown(output_text)

                    except Exception as e:
                        st.error(f"**Error loading output audio:** {e}")
            else:
                st.error("Output audio file not found. Please check if 'output_audio.mp3' was generated.")
        else:
            st.error("Error during inference execution.")
            st.code(result.stderr)
    except Exception as e:
        st.error(f"Exception occurred while running inference: {e}")



from singleLLM import run_LLM_model_evaluation

st.markdown("---")
st.subheader("🧒 Child Info & 🤖 LLM Evaluation")

# Input field for child's age
child_age = st.number_input("Enter the child's age:", min_value=1, max_value=7, step=1)

# Button to trigger evaluation
if st.button("Evaluate LLM Model"):

        with st.spinner("Evaluating the LLM model..."):
            run_LLM_model_evaluation_fullInference(child_age)
        st.success("LLM model evaluation completed successfully!")

        # Display content from evaluation.txt
        evaluation_file = "evaluation.txt"
        # evaluation_file = "example_evaluation.txt"
        if os.path.exists(evaluation_file):
            with open(evaluation_file, "r", encoding="utf-8") as file:
                evaluation_text = file.read()
            st.markdown("---")
            st.subheader("📄 Evaluation Results")
            st.text(evaluation_text)
        else:
            st.warning(f"File `{evaluation_file}` not found. Make sure it is created by the evaluation function.")





# --- Custom Styling ---
st.markdown(
    """
    <style>
    .stTextInput label {
        font-weight: bold;
        color: #333;
    }
    .stImage {
        border-radius: 10px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        transition: transform 0.2s ease-in-out;
    }
    .stImage:hover {
        transform: scale(1.01);
    }
    .stAudio {
        margin-top: 25px;
        border-radius: 10px;
        background-color: #e9f0f7;
        padding: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .stSuccess {
        background-color: #d4edda;
        color: #155724;
        border-radius: 5px;
        padding: 10px;
        margin-top: 10px;
    }
    .stWarning {
        background-color: #fff3cd;
        color: #856404;
        border-radius: 5px;
        padding: 10px;
        margin-top: 10px;
    }
    .stError {
        background-color: #f8d7da;
        color: #721c24;
        border-radius: 5px;
        padding: 10px;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
