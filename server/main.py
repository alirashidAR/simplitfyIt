from fastapi import FastAPI
from PIL import Image
import io
from image_generator_hf import generate_image
import cv2
import numpy as np

app = FastAPI()

@app.post("/generateimage")
async def generate_image_endpoint(inputs: str):
    image_bytes = generate_image(inputs)
    print("Generating character image...")

    # Save image to file
    with open("data/video/image.png", "wb") as f:
        f.write(image_bytes)

    # Convert image bytes to numpy array
    image = Image.open(io.BytesIO(image_bytes))
    image_np = np.array(image)

    # Convert RGB to BGR (OpenCV uses BGR format)
    image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    height, width, layers = image_np.shape
    video = cv2.VideoWriter('data/video/image.mp4', fourcc, 1, (width, height))

    # Write the frame to the video
    video.write(image_np)

    # Release the video writer
    video.release()

    return {"status": "success"}



@app.post('/generateSummary'):
async def generateSummary(inputs: str):
    