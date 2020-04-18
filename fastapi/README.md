# FastAPI

---

Documentation: https://fastapi.tiangolo.com

Source Code: https://github.com/tiangolo/fastapi

---

## Requirements

Python 3.6+

In my environment, I use `python_version = "3.7"`.

## Installation

`Pipenv`: https://github.com/pypa/pipenv 

From Nothing.

```
$ pipenv install
$ pipenv install fastapi
$ pipenv install uvicorn
```

From Pipfile.

```
$ pipenv install
```

## Minimum Example

### Create a file.

```main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

### Run it.

```
$ pipenv run uvicorn main:app --reload
```

Open your browser at http://127.0.0.1:8000/items/5?q=somequery.

You will see the JSON response as:

`{"item_id": 5, "q": "somequery"}`

You already created an API that:
- Receives HTTP requests in the paths / and /items/{item_id}.
- Both paths take GET operations (also known as HTTP methods).
- The path /items/{item_id} has a path parameter item_id that should be an int.
- The path /items/{item_id} has an optional str query parameter q.


### Interactive API docs

Now go to http://127.0.0.1:8000/docs.

You will see the automatic interactive API documentation (provided by Swagger UI):

## Alternative API docs

And now, go to http://127.0.0.1:8000/redoc.
