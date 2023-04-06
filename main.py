import requests

api_key = "0b0daa26364c4bbc901262ea88dbf733"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-03-06" \
      "&sortBy=publishedAt&apiKey=0b0daa26364c4bbc901262ea88dbf733"
requests = requests.get(url)
content = requests.json()
for article in content["articles"]:
      print(article["title"])
      print(article["description"])

