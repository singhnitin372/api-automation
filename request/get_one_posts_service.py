from utility import log_request_data
from utility.base_utility import get_base_uri
import requests
import allure


# Calling get_post_by_id service
@allure.step("Calling GET POST API by id : {id}")
def get_post_by_id(id):
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    base_url = get_base_uri()
    request_uri = base_url + "/posts/" + str(id)
    log_request_data.from_request(request_uri, headers, 'get_post_by_id')
    response = requests.get(request_uri)
    return response
