from fastapi import FastAPI
from .core.config import PROJECT_NAME
from mangum import Mangum

app = FastAPI(
    title=PROJECT_NAME,
    # if not custom domain
    # openapi_prefix="/Prod"
)


@app.get("/today")
def today():
    """
    Return today's schedule from the user's calendar.

    This path operation will:
    * return a map of events

    """
    return {"Today is a great day!"}


handler = Mangum(app, enable_lifespan=False)
