from fastapi import FastAPI
from pydantic import BaseModel
import hashlib

app = FastAPI()

# 1. Define the Pydantic model
class TextInput(BaseModel):
    text: str

# 2. Create the POST endpoint
@app.post("/generate")
async def generate_checksum(data: TextInput):
    """
    Accepts a JSON body with a 'text' field.
    Calculates an MD5 checksum of the text and returns it 
    along with a personalized welcome message.
    """
    # Convert string to bytes and hash it using MD5
    checksum = hashlib.md5(data.text.encode()).hexdigest()
    
    return {
        "checksum": checksum,
        "message": "Welcome, [Pista Madalina-Ioana]!"
    }
