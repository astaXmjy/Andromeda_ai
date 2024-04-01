import assemblyai as goku
import google.generativeai as genai
import pyaudio
import wave
import numpy as np
import time
import requests, json, time
import pyttsx3



CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
SILENCE_THRESHOLD = 7000
SILENCE_DURATION = 4
WAVE_OUTPUT_FILENAME = "dee.wav"

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
)


print("* sun rhi hu......😄😄😄😄😄")

frames = []
start_time = time.time()
silent_duration = 0


while True:
    data = stream.read(CHUNK)
    frames.append(data)
    audio_chunk = np.frombuffer(data, dtype=np.int16)
    energy = np.sum(audio_chunk**2) / len(audio_chunk)

    if energy < SILENCE_THRESHOLD:
        silent_duration += 1
    else:
        silent_duration = 0

    if silent_duration >= RATE / CHUNK * SILENCE_DURATION:
        break

print("* sun liya ab thoda sabar rakh bandar......😀😀😀😀😀")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b"".join(frames))
wf.close()


goku.settings.api_key = "a63abf7b770f4b5d80ad652878f9d89d"

audio_url = "dee.wav"


gemini_api_key = "AIzaSyD-w3B-jjyesP9f8ExJ5gd-Xd8PqXcUUPc"


genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel("gemini-pro")
gokuGenerator = goku.Transcriber()
gokuScript = gokuGenerator.transcribe(audio_url)

response = model.generate_content(gokuScript.text)


engine = pyttsx3.init()
engine.say(response.text)
engine.runAndWait()