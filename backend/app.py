import json
from fastapi import FastAPI, Request
from tools import get_pred, hard_matching, fuzzy_matching
from data.samples import attr_sample1

app = FastAPI()


@app.post('/predict')
async def predict(request: Request):
    content = await request.json()
    data = json.loads(content)['text']
    print(data)
    pred = get_pred(data)
    result = {'attributes_found': pred}
    user = hard_matching(attr_sample1, pred)
    if user is not None:
        result['user'] = user
    else:
        user, jaro_dist, threshold, final = fuzzy_matching(attr_sample1, pred)
        if final == 1:
            result['user'] = user
            result['jaro_thresholds'] = {k: str(v) for k, v in threshold.items()}
            result['jaro_results'] = {k: str(v) for k, v in jaro_dist.items()}
    print(result)
    return result
