import os
from sarvamai import SarvamAI
from api_key import API

client = SarvamAI(
    api_subscription_key=API
)

def get_latest_audio():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    audio_dir = os.path.join(BASE_DIR, "voice_inputs")
    files = [
        os.path.join(audio_dir, f)
        for f in os.listdir(audio_dir)
        if f.lower().endswith(".wav")
    ]

    if not files:
        raise FileNotFoundError("No audio files found in voice_inputs")

    latest_file = max(files, key=os.path.getctime)
    return latest_file

audio_path = get_latest_audio()

print(f"🎧 Using latest audio: {audio_path}")

with open(audio_path, "rb") as audio_file:
    response = client.speech_to_text.translate(
        file=audio_file,
        model="saaras:v2.5"
    )

print("📝 Response from Sarvam:")
print(response)