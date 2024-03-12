import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from api import home
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Serve static files (e.g., CSS, JS) from a folder named "static"
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(home.router)


if __name__ == "__main__":
    uvicorn.run("captcha_app:app", host="0.0.0.0", port=8889, reload=True)