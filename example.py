
import re
from typing import List

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI(title="String & Math Utilities")


class ConcatRequest(BaseModel):
    strings: List[str]
    separator: str = ""


@app.post("/concatenate")
def concatenate(body: ConcatRequest):
    return {"result": body.separator.join(body.strings)}


@app.get("/palindrome")
def check_palindrome(text: str = Query(..., min_length=1)):
    # Ignore case, spaces and punctuation ("A man, a plan, a canal: Panama")
    cleaned = re.sub(r"[^a-z0-9]", "", text.lower())
    return {"text": text, "is_palindrome": cleaned == cleaned[::-1]}



@app.get("/fibonacci")
def fibonacci(n: int = Query(..., ge=1, le=1000, description="Number of terms")):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return {"n": n, "sequence": seq}


@app.get("/reverse")
def reverse_string(text: str = Query(...)):
    return {"original": text, "reversed": text[::-1]}



@app.get("/celsius-to-fahrenheit")
def celsius_to_fahrenheit(celsius: float = Query(...)):
    return {"celsius": celsius, "fahrenheit": round(celsius * 9 / 5 + 32, 2)}