import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np


def record_audio(duration, path, samplerate=44100, channels=1):
    """
    Records audio from the default input device.

    Parameters:
    - duration: Duration in seconds to record.
    - path: Full path (including filename.wav) to save the recording.
    - samplerate: Sample rate (default: 44100 Hz).
    - channels: Number of audio channels (1 = mono, 2 = stereo).
    """
    print("Recording started...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")

    write(path, samplerate, audio)  # Save as WAV file
    print(f"Audio saved to: {path}")


# Example usage:
record_audio(duration=5, path="output.wav")
