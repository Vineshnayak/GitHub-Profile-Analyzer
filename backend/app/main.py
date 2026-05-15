from fastapi import FastAPI

from app.api.routes.profile import (
    router as profile_router
)

from app.api.routes.resume import (
    router as resume_router
)

from app.api.routes.wrapped import (
    router as wrapped_router
)

app = FastAPI(
    title="GitHub Profile Analyzer",
    version="1.0.0"
)

app.include_router(
    profile_router,
    prefix="/profile",
    tags=["Profile Analysis"]
)

app.include_router(
    resume_router,
    prefix="/resume",
    tags=["Resume Generator"]
)

app.include_router(
    wrapped_router,
    prefix="/wrapped",
    tags=["GitHub Wrapped"]
)


@app.get("/")
def root():

    return {

        "message":
            "GitHub Profile Analyzer API Running"
    }