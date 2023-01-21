# Proxy judge

## Python proxy judge running with sanic

You can use this to test your proxies. https://pyjudge.vercel.app/

## Usage
1. Python
```python
import requests

proxy = "YOUR PROXY"
url = "https://pyjudge.vercel.app/"

with requests.Session() as s:
    s.proxies = {
        "http": proxy, # http can be replaced with https
    }
    r = s.get(url)
    print(r.json())
```
More languages coming soon. Or maybe not 🤷‍♂️.
