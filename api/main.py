from fastapi import FastAPI
from routers import users, groups, messages, conversations
from models import create_db
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

router = FastAPI(csrf=True)
router.mount("/static", StaticFiles(directory="static"), name="static")
db = create_db()

db.connect()

origins = [
    "http://localhost:3000",  
    "http://localhost:8000"
]

router.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@router.get("/")
def root_access():
    return {"message": "Hello World"}


router.include_router(users.router)
router.include_router(groups.router)
router.include_router(messages.router)
router.include_router(conversations.router)

