import requests

def search_box(query, access_token):
    url = "https://api.box.com/2.0/search"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "query": query,
        "type": "file",
        "content_types": "name,description,file_content",
        "limit": 5
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(f"Message: {response.text}")
        return None