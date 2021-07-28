from utility import log_request_data
from utility.base_utility import get_base_uri
import requests
import allure


# Calling delete_post service
@allure.step('Calling DELETE POSTS API with id: {id} ')
def delete_post(id):
    base_url = get_base_uri()
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    request_uri = base_url + "/posts/" + str(id)
    log_request_data.from_request(request_uri, headers, 'delete_posts')
    response = requests.delete(request_uri, headers=headers)
    return response
