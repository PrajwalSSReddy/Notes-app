from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from models.notes import Note
from config.db import conn
from fastapi.templating import Jinja2Templates
from schemas.notes import NoteEntity,NotesEntity

note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    newdocs = []
    docs = conn.notes.notes.find({})
    for doc in docs:
        newdocs.append({
            'id':doc['_id'],
            'title':doc['title'],
            'desc': doc['desc'],
            'important':doc['important']
        })
    return templates.TemplateResponse("index.html",{"request": request, "newdocs": newdocs})


@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    dictform = dict(form)
    print(dictform)
    # dictform['important'] = True if dictform['important'] else False
    # note = conn.notes.notes.insert_one(dictform)
    return {'Succesful': True}