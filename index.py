from fastapi import FastAPI
from routes.routes_note import note
from fastapi.staticfiles import StaticFiles

app = FastAPI()



app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(note)