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
    # Calculate a simple hex checksum of the input text
    checksum = hashlib.md5(data.text.encode()).hexdigest()
    
    return {
        "checksum": checksum,
        "message": "Welcome, [Your Name]!"
    }
