import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def mygemai(prompt):
    client =  genai.configure(api_key=os.getenv("GENAIAPI_KEY"))
    model =   genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat()
    response = chat.send_message(prompt)
    final_response = response.text.replace("#","").replace("*","")
    return final_response
    