from utility import read_json, log_request_data
from utility.base_utility import get_base_uri
import requests
import allure


# Calling create_new_post service
@allure.step('Calling CREATE NEW POST API ')
def create_new_post():
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    base_url = get_base_uri()
    data = read_json.readfile("create_new_post.json")
    request_uri = base_url + "/posts"
    log_request_data.from_request(request_uri, headers, 'create_new_post')
    response = requests.post(url=request_uri, data=data)
    return response
