from fastapi import FastAPI
from routers import users, groups, messages, conversations
from routers import users

router = FastAPI()


@router.get("/")
def root_access():
    return {"message": "Hello World"}


router.include_router(users.router)
router.include_router(groups.router)
router.include_router(messages.router)
router.include_router(conversations.router)
