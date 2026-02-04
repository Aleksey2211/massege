from fastapi import FastAPI
import uvicorn

from users.router import router as users_router


app = FastAPI()


app.include_router(users_router)


@app.get("/")
def greet():
    return "Hello World!"


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)
