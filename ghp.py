#ghp = google home page
import requests  # imports the requests module to make HTTP requests
headers = {  # creates a dictionary of HTTP headers
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"  # fakes a browser so Google doesn't block the request
}
res = requests.get("https://www.google.com", headers=headers)  # sends a GET request to Google with headers
print(res.status_code)  # prints the HTTP status code (e.g. 200 means OK)

print(res.text[:100])  # prints the first 1000 characters of the HTML response

print(res)
print(res.url)