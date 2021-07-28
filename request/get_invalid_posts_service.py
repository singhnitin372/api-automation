from utility import log_request_data
from utility.base_utility import get_base_uri
import requests
import allure


# Calling get_invalid_post service
@allure.step("Calling GET INVALID POST API")
def get_invalid_post():
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    base_url = get_base_uri()
    request_uri = base_url + "/invalidposts"
    log_request_data.from_request(request_uri, headers, 'get_invalid_posts')
    response = requests.get(request_uri)
    return response
