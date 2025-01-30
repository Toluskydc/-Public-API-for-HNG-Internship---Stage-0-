from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/", status_code=status.HTTP_200_OK)
async def get_info():
    return {
        "email": "booktolusky@gmail.com",
        "current_datetime": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "github_url": "https://github.com/Toluskydc/-Public-API-for-HNG-Internship---Stage-0-"
    }
