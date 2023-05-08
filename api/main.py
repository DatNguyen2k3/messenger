from fastapi import FastAPI
from routers import users, groups, messages, conversations
from models import create_db
from fastapi.staticfiles import StaticFiles

router = FastAPI(csrf=True)
router.mount("/static", StaticFiles(directory="static"), name="static")
db = create_db()

db.connect()

@router.get("/")
def root_access():
    return {"message": "Hello World"}


router.include_router(users.router)
router.include_router(groups.router)
router.include_router(messages.router)
router.include_router(conversations.router)

