from starlette.datastructures import CommaSeparatedStrings
import os

ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", ""))
PROJECT_NAME = "TodayApp"
