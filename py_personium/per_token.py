import requests

def get_token(cell_url, cell_account):
    api = cell_url + '__token'
    headers = {
        'Accept': 'application/json',
        'Content-Type' : 'application/x-www-form-urlencoded'
    }
    params = "grant_type=password&username=" + cell_account['user'] + "&password=" + cell_account['password']
    res = requests.post(api, headers=headers, data=params)
    return res