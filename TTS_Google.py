from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os







def Generate_TTS(text,save_path):
    # text = "ילַד הוֹלֵךְ לְבֵית הַסָּפֶר"

    gTTS(text=text, lang='iw').save(save_path)

def Play_Audio(audio_file_path):
    try:
        audio = AudioSegment.from_mp3(audio_file_path)
        play(audio)
        print(f"Audio file '{audio_file_path}' played successfully.")
    except Exception as e:
        print(f"Error playing audio with pydub: {e}")
        print("Make sure ffmpeg is installed and accessible in your system's PATH.")

if __name__ == "__main__":
    text = 'קוֹרְאִים לִי רוֹבּוֹ-שָׁאוּל וַאֲנִי מַכִּיר בָּנוֹת מֵאַרְגֶּנְטִינָה וּבָנִים מִבְּרָזִיל.'
    text = "הוּא קִבֵּל גְּלִידָה"

    audio_path = "google_audio1.mp3"
    Generate_TTS(text,audio_path)
    Play_Audio(audio_path)