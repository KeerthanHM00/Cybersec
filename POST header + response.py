import urllib.request
import urllib.parse
import gzip

# Define the target URL
url = "http://testphp.vulnweb.com"

# Print the headers for the POST request
headers = {
    "Host": "testphp.vulnweb.com",
    "Content-Length": "28",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "http://testphp.vulnweb.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "http://testphp.vulnweb.com/search.php?test=query",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "close",
}

# POST data
search= str(input("what do you want to search for: "))
post_data = "searchFor="+search+"&goButton=go"
print(type(post_data))
encoded_data = post_data.encode('utf-8')

print("POST Request Headers:")
for key, value in headers.items():
    print(f"{key}: {value}")

# Send a POST request
try:
    request = urllib.request.Request(f"{url}/search.php?test=query", data=encoded_data, headers=headers, method='POST')
    response = urllib.request.urlopen(request)


    # Print the content of the response
    content = response.read()
    compressed_data = content
    decompressed_data = gzip.decompress(compressed_data)
    utf8_data = decompressed_data.decode('utf-8')
    print("\nResponse data:")
    print(utf8_data)

except Exception as e:
    print(f"Error: {e}")



