import requests

URL = r'http://localhost:5000/' #URL
count=0
while(1):
  res = requests.get(URL)
  print(count)
  count+=1
  if('flag{' in res.text):
    print(res.text)
    break