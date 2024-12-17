import requests
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.content

def generate_image(prompt):
    try:
        # Sending the request to generate an image
        image_bytes = query({"inputs": prompt})
        
        # Load the image with PIL
        image = Image.open(io.BytesIO(image_bytes))
        image.show()  # Opens the image in the default image viewer
        
        # Save the image locally
        image.save("image.png")  # Saves the image as "generated_image.png" in the current directory
        print("Image saved as 'image.png'")
    
    except Exception as e:
        print(f"Error: {e}")

