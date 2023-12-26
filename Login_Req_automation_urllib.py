import urllib.request
import urllib.parse
import gzip

# Define the target URL
url = "http://139.144.1.145/index.php/index/login/signIn"
# Print the headers for the POST request
headers = {
    "Host": "139.144.1.145",
    "Content-Length": "93",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36",
    "Origin": "http://139.144.1.145",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "http://139.144.1.145/index.php/index/login",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "OJSSID=06nnugivpmcpq386r47bafr9bp",
    "Connection": "close",
}

# POST data
usr_name= str(input("username: ")) #username accepting variable
pswd= str(input("password: ")) #password accepting variable
post_data = "csrfToken=d570b82aff7b044367832cf895d6589d&source=&username="+usr_name+"&password="+pswd+"&remember=1"

encoded_data = post_data.encode('utf-8')

print("POST Request Headers:")
for key, value in headers.items():
    print(f"{key}: {value}")

# Send a POST request
try:
    request = urllib.request.Request(url, data=encoded_data, headers=headers, method='POST')
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



