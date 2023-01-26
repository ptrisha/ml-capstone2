import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

# This is url for an image of a mountain
data = {'url': 'https://unsplash.com/photos/dR_q93lfaTw/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjc0NjQ1Njc3&force=true&w=640'}

result = requests.post(url, json=data).json()
print(result)
