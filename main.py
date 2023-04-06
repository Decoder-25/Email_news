import requests
from send_emails import send_email

api_key = "0b0daa26364c4bbc901262ea88dbf733"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-03-06" \
      "&sortBy=publishedAt&apiKey=0b0daa26364c4bbc901262ea88dbf733"
requests = requests.get(url)
content = requests.json()

body = ""
for article in content["articles"]:
    if article["description"] is not None:
        body = body + article["title"] + "\n" + article[
            "description"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
