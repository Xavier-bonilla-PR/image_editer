import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv('AI_KEY'))

def image_with_mask():
    response = client.images.edit(
    model="dall-e-2",
    image=open("permutation_diagram.png", "rb"),
    mask=open("permutation_mask.png", "rb"),
    prompt="A circular diagram with an arrow pointing from X1 to X3",
    n=4,
    size="1024x1024"
    )
    image_url = response.data[0].url 
    return print(image_url)

def variation():
    response = client.images.create_variation(
    model="dall-e-2",
    image=open("permutation_diagram.png", "rb"),
    n=1,
    size="1024x1024"
    )

    image_url = response.data[0].url
    return print(image_url)

image_with_mask()
#variation()
