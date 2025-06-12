import TTS_Google as TTS
import singleLLM
import whisperOpenAI

def save_input(text):
    try:
        with open("users_answers.txt", "a", encoding="utf-8") as file:
            file.write(text_input + "\n")  # Add a newline character for better readability
        print(f"Successfully appended: '{text_input}' to 'user.txt'")
    except FileNotFoundError:
        print("Error: 'user.txt' not found. Please make sure the file exists in the same directory.")
    except Exception as e:
        print(f"An error occurred: {e}")


## Step By Step Inference


#Audio Input
input_audio = "input_audio.mp3"
input_audio = "a1_gotIceCream.mp3"
# TTS.Play_Audio(input_audio)


#Audio Transcription using Whisper
# text_input = whisperOpenAI.whisper_transcript(input_audio)
text_input = "הוא קיבל גלידה"
# text_input = "הוא קיבלה גלידה"
save_input(text_input) # Save Input Text to Run in LLM


#LLM processes the text input
text_correct_syntax = singleLLM.run_LLM_model_syntax(text_input)
# text_correct_syntax = "הַיֶּלֶד משְׂחָק בְּקוֹביוֹת"
with open("outputLLM.txt", "w", encoding="utf-8") as file:
    file.write(text_correct_syntax) #Save LLM result

#####  Nikud   ######
## Nikud Model Needs to be added ##
## (So TTS Model will be accurate) ##


# Make LLM result (after Nikud) a mp3 audio.
audio_path_output = "output_audio.mp3"
TTS.Generate_TTS(text_correct_syntax,audio_path_output)
TTS.Play_Audio(audio_path_output)



