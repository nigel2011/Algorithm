
import os
import requests

r = requests.get('https://naver.com/')
#print(r)
#print(r.url)

print("welcome to IsitDown.py!")
print("please wrtie a URL or URLs you want to check. (separated by comma)")

url = link = input ("")
if r.status_code == 200:
  print(r.url,"is up!")
  do you want to start over? y/n")

