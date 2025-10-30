import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from .env
load_dotenv()

# Initialize the client
client = InferenceClient(
    provider="fal-ai",
    api_key=os.environ["HF_TOKEN"],  # token loaded from .env
)

# Generate image
image = client.text_to_image(
    "A futuristic city skyline at sunset",
    model="black-forest-labs/FLUX.1-dev",
)

# Save the image
image.save("generated_image.png")
print("✅ Image saved as generated_image.png")
