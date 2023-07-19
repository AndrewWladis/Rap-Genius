import openai
import re
from picture_api import search_photo_by_name
import os
from dotenv import load_dotenv

def remove_text_between_hash_and_space(string):
  return re.sub(r'[^\w\s]', '', string.replace('"', ""))

def ai_req(character_one, character_two):
  load_dotenv()
  photo = search_photo_by_name(character_one)
  OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')
  openai.organization = "org-ElxhBoDrwZrCYkMxuZnAFit0"
  openai.api_key = OPEN_AI_KEY
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": f'imagine you are {character_one} in a rap battle, battling to {character_two}. Please respond in 150 characters. No hashtags'}
    ]
  )
  response = remove_text_between_hash_and_space(completion.choices[0].message.content + " ")
  
  return {
    "response": response,
    "photo": photo
  }