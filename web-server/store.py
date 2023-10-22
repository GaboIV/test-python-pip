import requests 

api_url_categories  = 'https://api.escuelajs.co/api/v1/categories'

def get_categories():
    req = requests.get(api_url_categories)
    # print(req.status_code)
    # print(req.text)
    categories = req.json()
    for category in categories:
        print(category['name'])