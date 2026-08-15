from fastapi import FastAPI
from fastapi import Response

app = FastAPI()


@app.get("/")
async def root():
    res = Response(
        content='{"message": "Hey cass"}',
        status_code=418,
        headers=None,
        media_type="application/json",
        background=None,
    )
    return res


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
