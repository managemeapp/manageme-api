FROM python:3.7

RUN pip install fastapi uvicorn mangum pydantic

EXPOSE 8080

COPY ./today_app /today_app

CMD ["uvicorn", "today_app.main:app", "--host", "0.0.0.0", "--port", "8080"]
