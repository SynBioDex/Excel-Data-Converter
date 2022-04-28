import requests
import websocket
import json

# post the chemical name for a specific chemical
def flapjack_post_chemical_name_request(chemical, access_token):
    flapjack_post_chemical_name_url = "http://3.128.232.8:8000/api/chemical/" 
    headers = {
        'Authorization': 'Bearer ' + access_token}
    return requests.post(flapjack_request_assay_id_url, headers=headers)

#get the chemical flapjack ID for a specific chemical