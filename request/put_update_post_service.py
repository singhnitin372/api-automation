from utility import read_json, log_request_data
from utility.base_utility import get_base_uri
import requests
import allure


# Calling update_new_post service
@allure.step("Calling UPDATE NEW POST API by id : {id}")
def update_new_post(id):
    d = {'id': id}
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    base_url = get_base_uri()
    data = read_json.readfile("update_post.json", d)
    request_uri = base_url + "/posts/" + str(id)
    log_request_data.from_request(request_uri, headers, 'update_post')
    response = requests.put(url=request_uri, data=data)
    return response
