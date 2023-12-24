import urllib.request

# Define the target URL
url = "www.example.com"

# Print the headers for the GET request
headers = {
    "Host": url,
    "Sec-Ch-Ua": '"Chromium"; v="119", "Not?A Brand"; v="24"',
    "Sec-Ch-Ua-Mobile": "70",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US, en;q=0.9",
    "Priority": "u=0, 1",
    "Connection": "close"
}

print("GET Request Headers:")
for key, value in headers.items():
    print(f"{key}: {value}")

# Send a GET request
response = urllib.request.urlopen(f"https://{url}/")

# Print the content of the response
print("\nResponse data:")
print(response.read().decode('utf-8'))
