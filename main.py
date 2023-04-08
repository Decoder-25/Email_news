import requests
from send_emails import send_email


topic = "tesla"
api_key = "0b0daa26364c4bbc901262ea88dbf733"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-03-08" \
      "&sortBy=publishedAt&" \
      "apiKey=0b0daa26364c4bbc901262ea88dbf733&" \
      "language=en"
requests = requests.get(url)
content = requests.json()

body = ""
for article in content["articles"][:20]:
    if article["description"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" + article[
            "description"] + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
