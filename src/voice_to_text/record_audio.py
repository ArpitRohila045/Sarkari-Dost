import sounddevice as sd
from scipy.io.wavfile import write
import os
from datetime import datetime

fs = 16000
duration = 5

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
voice_dir = os.path.join(BASE_DIR, "voice_inputs")
os.makedirs(voice_dir, exist_ok=True)

filename = os.path.join(
    voice_dir,
    f"input_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
)

print("🎙 Speak now...")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()

write(filename, fs, audio)
print(f"✅ Saved: {filename}")
