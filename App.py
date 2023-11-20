from google.cloud import speech_v1p1beta1 as speech
from openai import OpenAI

client = speech.SpeechClient.from_service_account_file('key.json')
file_name = "Audio.mp3"

with open (file_name, 'rb') as f:
    mp3_data = f.read()

audio_file = speech.RecognitionAudio(content=mp3_data)
config = speech.types.RecognitionConfig(
    sample_rate_hertz=8000,
    language_code='es_CL',
    enable_automatic_punctuation=True)

response = client.recognize(
    config=config,
    audio=audio_file
)

client = OpenAI(
    api_key="API_KEY",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": 'Puedes generar un apunte, considerando lo siguiente: '+response
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion)