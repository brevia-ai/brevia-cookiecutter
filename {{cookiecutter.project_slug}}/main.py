"""API endpoint definitions with FastAPI."""
from os import environ
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from brevia.routers.app_routers import add_routers

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)
add_routers(app)

# Add your custom endpoints here...

if __name__ == '__main__':
    load_dotenv()
    run_opts = {
        'port': int(environ.get('API_PORT', '8000')),
        'host': '0.0.0.0',
        'reload': True,
    }
    uvicorn.run('main:app', **run_opts)
