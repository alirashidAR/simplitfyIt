from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from image_generator_hf import generate_image as hf_generate_image
from summaryGenerator import generateSummary
from TTS import generate_and_download_audio
import io
from time import sleep
from PIL import Image
import requests
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://ajcnjcgigpokmmjlkmbmbhpagflkohok"],  # Allow the Chrome extension
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}

# Helper functions to generate summary, audio, and image
async def generate_summary(way: str, text: str):
    summary = generateSummary(way, text)
    return summary

async def generate_audio(text: str, type='M'):
    audio_path = os.path.join("audio.mp3")  # Stored in same directory as main.py
    generate_and_download_audio(text, audio_path,type='M')
    return audio_path

async def generate_image_from_inputs(inputs: str):
    payload = {"inputs": inputs}
    response = requests.post(API_URL, headers=headers, json=payload)
    image_bytes = response.content
    image = Image.open(io.BytesIO(image_bytes))
    image.save("image.png")
    return "image.png"


# Main endpoint to handle the entire process
@app.post("/generate_final_video")
async def generate_final_video(text: str, way: str, inputs: str, type: str):
    # Step 1: Generate the summary from the text
    print("Generating summary...")
    summary = await generate_summary(way, text)
    if not summary:
        raise HTTPException(status_code=500, detail="Failed to generate summary")
    print("Summary generated successfully")



    # Step 2: Generate the audio from the summary
    print("Generating audio...")
    audio_path = await generate_audio(summary,type)
    if not audio_path:
        raise HTTPException(status_code=500, detail="Failed to generate audio")
    print("Audio generated successfully")


    
    # Step 3: Generate the image
    print("Generating image...")
    image_path = await generate_image_from_inputs(inputs)
    if not image_path:
        raise HTTPException(status_code=500, detail="Failed to generate image")
    print("Image generated successfully")

    print('Generating the final video')
    # Step 4: Save files locally to send to Flask for lipsync processing
    media_filename = "image.png"
    audio_filename = "audio.mp3"

    # Step 5: Send files to Flask for lipsync processing
    flask_url = "http://127.0.0.1:5000/upload"  # Flask server URL
    with open(media_filename, "rb") as media_file, open(audio_filename, "rb") as audio_file:
        files = {
            "media": media_file,
            "audio": audio_file
        }
        response = requests.post(flask_url, files=files)

    # Handle Flask server's response
    if response.status_code == 200:
        processed_video = response.json().get("processed_video")
        # Send the video file to the client
        sleep(2)
        video_path = r"D:\ho\Wav2Lip\results\result_voice.mp4"
        return FileResponse(video_path, media_type="video/mp4", filename="result_voice.mp4")

    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to process lipsync")
    

# @app.post("/generate_final_video_premade")
# async def generate_final_video():
#     # # Step 1: Generate the summary from the text
#     # summary = await generate_summary(way, text)
#     # if not summary:
#     #     raise HTTPException(status_code=500, detail="Failed to generate summary")

#     # # Step 2: Generate the audio from the summary
#     # audio_path = await generate_audio(summary)
#     # if not audio_path:
#     #     raise HTTPException(status_code=500, detail="Failed to generate audio")

#     # # Step 3: Generate the image
#     # image_path = await generate_image_from_inputs(inputs)
#     # if not image_path:
#     #     raise HTTPException(status_code=500, detail="Failed to generate image")

#     # Step 4: Save files locally to send to Flask for lipsync processing
#     media_filename = "image.png"
#     audio_filename = "audio.mp3"

#     # Step 5: Send files to Flask for lipsync processing
#     flask_url = "http://127.0.0.1:5000/upload"  # Flask server URL
#     with open(media_filename, "rb") as media_file, open(audio_filename, "rb") as audio_file:
#         files = {
#             "media": media_file,
#             "audio": audio_file
#         }
#         response = requests.post(flask_url, files=files)

#     # Handle Flask server's response
#     if response.status_code == 200:
#         processed_video = response.json().get("processed_video")
#         return {"message": "Final video generated successfully", "processed_video": processed_video}
#     else:
#         raise HTTPException(status_code=response.status_code, detail="Failed to process lipsync")

@app.post('/')
async def get_image(text: str):
    image_path = await generate_image_from_inputs(text)
    return {"image_path": image_path}
