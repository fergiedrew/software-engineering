# importing the requests library
import requests
  
# api-endpoint
URL = "https://pastebin.com/api/api_post.php"
  
# location given here
location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location}
  
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
  
# extracting data in json format
data = r.json()
print(data)
