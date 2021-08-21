import json
from fastapi import FastAPI, Request


app = FastAPI()


@app.post('/predict')
async def predict(request: Request):
    content = await request.json()
    inn, data = convert_json_to_dataset(json.loads(content))
    result = {str(inn): str(model.predict(data)[0])}
    print(result)
    return result
