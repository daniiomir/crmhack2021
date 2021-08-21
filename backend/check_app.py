import json
import requests
from data.json_samples import json_sample1

if __name__ == '__main__':
    r = requests.post('http://localhost:55555/predict', json=json.dumps(json_sample1, ensure_ascii=False))
    print(r)
    result = r.json()
    print(result)