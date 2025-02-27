import os
from dotenv import load_dotenv
from image_helpers import get_image_pixels, render_pixels

environment = os.getenv("ENVIRONMENT", "local")
load_dotenv(f".env.{environment}")

env_type = os.getenv("ENV_TYPE", "local")

print(f"Environment: {env_type}")    


# This function fetches pixel data from an image URL
# Use the functions above to fetch pixel data and render the original data
url = "https://www2.eecs.berkeley.edu/Faculty/Photos/Homepages/pamelafox.jpg"
pixel_data = get_image_pixels(url)
render_pixels(pixel_data)
