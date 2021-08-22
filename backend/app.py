import json
from fastapi import FastAPI, Request
from tools import get_pred

app = FastAPI()


@app.post('/predict')
async def predict(request: Request):
    content = await request.json()
    data = json.loads(content)['text']
    print(data)
    result = get_pred(data)
    print(result)
    return result
