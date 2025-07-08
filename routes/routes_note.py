from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, noteEntities
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from bson.objectid import ObjectId


note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs =[]
    for doc in docs:
        newDocs.append({
            "id" : doc["_id"],
            "title" : doc["title"],
            "desc" : doc["desc"],
            "important" : doc["important"]
        })

    return templates.TemplateResponse(
        "index.html", {"request": request, "newDocs" : newDocs}
    )

@note.post("/")
async def create_item(request:Request):
    form = await request.form()
    # print(form)
    dictform = dict(form)
    dictform["important"] = dictform.get("important") == "on"

    note = conn.notes.notes.insert_one(dictform)
    return RedirectResponse(url="/", status_code=303)



@note.get("/delete/{note_id}")
async def delete_note(note_id:str):
    conn.notes.notes.find_one_and_delete({"_id":ObjectId(note_id)})
    return RedirectResponse(url="/", status_code=303)


@note.get("/update/{note_id}", response_class=HTMLResponse)
async def get_update_page(request:Request, note_id:str):
    doc = conn.notes.notes.find_one({"_id":ObjectId(note_id)})

    note_data = {
        "id" : str(doc["_id"]),
        "title" : doc["title"],
        "desc" : doc["desc"],
        "important" : doc["important"]
    }

    return templates.TemplateResponse("update.html", {"request":request, "note":note_data})


@note.post("/update/{note_id}")
async def update_note(note_id:str, request:Request):
    form_data = await request.form()
    note_dict = dict(form_data)

    note_dict["important"] = note_dict.get("important") == "on"


    conn.notes.notes.find_one_and_update(
        {"_id":ObjectId(note_id)},
        {"$set": note_dict}
    )


    return RedirectResponse(url="/", status_code=303)