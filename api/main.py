import socket

from fastapi import FastAPI

app = FastAPI(title="FastAPI Microservice Example")


@app.get("/")
def root():
    return {"message": "Hello from FastAPI microservice!"}


@app.get("/health")
def health_check():
    hostname = socket.gethostname()
    return {"status": "ok", "pod": hostname}
