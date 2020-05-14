from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(
    title=PROJECT_NAME,
    # if not custom domain
    # openapi_prefix="/Prod"
)


@app.get("/today")
def pong():
    """
    Return today's schedule from the user's calendar.

    This path operation will:
    * return a map of events

    """
    return {"Today is a great day!"}


handler = Mangum(app, enable_lifespan=False)
