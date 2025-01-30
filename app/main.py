import os
import uvicorn

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
        "current_datetime": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "github_url": "https://github.com/Toluskydc/-Public-API-for-HNG-Internship---Stage-0-"
    }



if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)