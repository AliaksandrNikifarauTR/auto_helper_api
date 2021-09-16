import uvicorn
from fastapi import FastAPI


app = FastAPI()  # noqa: pylint=invalid-name


@app.get("/")
def read_root():
    return {'data': 'Hello world!!!!!!'}


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=False, root_path="/")