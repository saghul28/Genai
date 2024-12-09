from fastapi import APIRouter,Form
from fastapi.responses import JSONResponse
from myai import genai

router = APIRouter()

@router.post("/aptitude")
def generate_aptitude(topic:str=Form(...)):
   try:
       prompt =(
           f"Generate 3 aptitude questions with the following requirements in this {topic}:"
            f"Each question should have 4 answer options (labeled A, B, C, D)"
            f"Provide the correct answer for each question."
            f"For each question, explain why the correct answer is right."
            f"For each incorrect answer option, give a brief explanation of why it is incorrect."
            f"Make sure the questions are clear, suitable for general aptitude tests, and cover a mix of {topic}")
       response  = genai(prompt)
       return JSONResponse(content={"result":response})
   except Exception as e:
       return JSONResponse({"error":str(e)})
       
    
   