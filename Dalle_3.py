import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv('AI_KEY'))

response = client.images.generate(
  model="dall-e-3",
  #I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS
  prompt="a black cat in a cherry blossom garden",
  #1024x1024, 1024x1792 or 1792x1024 pixels
  size="1024x1024",
  #hd or standard
  quality="standard",
  #How many images you want
  n=1,
)
#Each image can be returned as either a URL or Base64 data, using the response_format parameter. URLs will expire after an hour.
image_url = response.data[0].url
print(image_url)
