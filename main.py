import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data from JSON file
with open("q-vercel-python.json", "r") as file:
    student_marks = json.load(file)

@app.get("/api")
def get_marks(name: list[str]):
    marks = [student_marks.get(n, 0) for n in name]
    return {"marks": marks}
