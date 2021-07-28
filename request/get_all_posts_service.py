from utility import log_request_data
from utility.base_utility import get_base_uri
import requests
import allure


# Calling get_all_posts service
@allure.step("Calling the GET ALL POSTS API ")
def get_request():
    base_url = get_base_uri()
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    request_uri = base_url + "/posts"
    log_request_data.from_request(request_uri, headers, 'get_all_posts')
    response = requests.get(request_uri)
    return response
