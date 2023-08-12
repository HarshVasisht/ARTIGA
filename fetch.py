import requests
import io
from PIL import Image

# def fetch_photo(query):
#     api_key = 'X9q6GfelLaToTEu7DUeEy1AczaqPYbQGEaaTVMc4e88PaP7CyMgyjwJI' 

#     url = 'https://api.pexels.com/v1/search'
#     headers = {
#         'Authorization': api_key,
#     }

#     params = {
#         'query': query,
#         'per_page': 2,
#     }

#     response = requests.get(url, headers=headers, params=params)

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         data = response.json()
#         photos = data.get('photos', [])
#         # print(photos)
#         if photos:
#             src_original_url = photos[0]['src']['original']
#             img_list = [photos[0]['src']['original'], photos[1]['src']['original']]
#             return src_original_url, img_list
#         else:
#             print("No photos found for the given query.")
#     else:
#         print(f"Error: {response.status_code}, {response.text}")
    
    # return None

# Example usage of the function
# query = input("pass the topic:")
# query = 'Circle'
# src_original_url, img_list = fetch_photo(query)
# if src_original_url and img_list:
#     print(f"Original URL for query '{query}': {img_list[0]}, {img_list[1]}")


def fetch_photo(query):
    api_key = 'X9q6GfelLaToTEu7DUeEy1AczaqPYbQGEaaTVMc4e88PaP7CyMgyjwJI' 

    url = 'https://api.pexels.com/v1/search'
    headers = {
        'Authorization': api_key,
    }

    params = {
        'query': query,
        'per_page': 1,
    }

    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        photos = data.get('photos', [])
        # print(photos)
        if photos:
            src_original_url = photos[0]['src']['original']
            # img_list = [photos[0]['src']['original'], photos[1]['src']['original']]
            return src_original_url
        else:
            print("No photos found for the given query.")
    else:
        print(f"Error: {response.status_code}, {response.text}")
    
    return None
q = "AI"
image_url = fetch_photo(q)
image_response = requests.get(image_url)
img = Image.open(io.BytesIO(image_response.content))

print(f"image_response : {image_response}")
print(f"image_url : {image_url}")