import requests
import pprint

def printResponse(res):
    print('<<response>>')
    print('<status code>')
    pprint.pprint(res.status_code)
    print('<header>')
    pprint.pprint(res.headers)
    print('<response body>')
    pprint.pprint(res.json())
    return