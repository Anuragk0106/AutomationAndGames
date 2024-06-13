import sounddevice as sd
import wavio
import numpy as np
import os

def record_audio(duration, filename, samplerate=44100):
    """
    Record audio for a given duration and save it to a WAV file.

    Parameters:
    - duration: Duration of the recording in seconds.
    - filename: Name of the file where the audio will be saved.
    - samplerate: Sampling rate of the recording. Default is 44100 Hz.
    """
    print("Recording...")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype=np.int16)
    sd.wait()  # Wait until the recording is finished
    print("Recording finished.")
    
    # Save the recorded audio data as a WAV file
    wavio.write(filename, audio_data, samplerate, sampwidth=2)
    print(f"Audio saved as {filename}")

if __name__ == "__main__":
    # Print the current working directory
    current_directory = os.getcwd()
    print(f"Current working directory: {current_directory}")
    
    # Get duration and filename from user
    duration = float(input("Enter the duration of the recording in seconds: "))
    filename = input("Enter the name of the output file (e.g., output.wav): ")
    
    # Record and save the audio
    record_audio(duration, filename)
