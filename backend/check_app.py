import json
import requests
from data.samples import sample1, sample2, sample3, sample4

if __name__ == '__main__':
    json_sample1 = {'text': sample1}
    r = requests.post('http://localhost:55555/predict', json=json.dumps(json_sample1, ensure_ascii=False))
    print(r)
    result = r.json()
    print(result)

    json_sample1 = {'text': sample2}
    r = requests.post('http://localhost:55555/predict', json=json.dumps(json_sample1, ensure_ascii=False))
    print(r)
    result = r.json()
    print(result)

    json_sample1 = {'text': sample3}
    r = requests.post('http://localhost:55555/predict', json=json.dumps(json_sample1, ensure_ascii=False))
    print(r)
    result = r.json()
    print(result)

    json_sample1 = {'text': sample4}
    r = requests.post('http://localhost:55555/predict', json=json.dumps(json_sample1, ensure_ascii=False))
    print(r)
    result = r.json()
    print(result)
