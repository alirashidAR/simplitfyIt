import requests
import json

def generate_and_download_audio(text, audio_filename='downloaded_audio.mp3', type='M'):
    voiceId = "en-US-miles"
    if type =='M':
        voiceId = "en-US-miles"
    else:
        voiceId = "en-US-natalie"

    url = "https://api.murf.ai/v1/speech/generate"

    payload = json.dumps({
        "voiceId": voiceId,
        "style": "Promo",
        "text": text,
        "rate": 0,
        "pitch": 0,
        "sampleRate": 48000,
        "format": "MP3",
        "channelType": "MONO",
        "pronunciationDictionary": {},
        "encodeAsBase64": False,
        "variation": 1,
        "audioDuration": 0,
        "modelVersion": "GEN2"
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'api-key': ''
    }

    # Sending POST request to generate speech
    response = requests.post(url, headers=headers, data=payload)

    # Check if the response was successful
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json()

        # Extract the audio URL from the response
        audio_url = response_data.get("audioFile")

        if audio_url:
            # Send GET request to download the audio file
            audio_response = requests.get(audio_url)

            # Check if the audio request was successful
            if audio_response.status_code == 200:
                # Save the audio content to a file
                with open(audio_filename, 'wb') as file:
                    file.write(audio_response.content)
                print(f"Audio downloaded successfully as {audio_filename}!")
            else:
                print(f"Failed to download audio. Status code: {audio_response.status_code}")
        else:
            print("Audio file URL not found in the response.")
    else:
        print(f"Failed to generate speech. Status code: {response.status_code}")

