import json
import pytest
import allure
from request import put_update_post_service, get_one_posts_service
from schemas import put_update_posts_service_schema
from utility import read_json, log_response_data
from utility.log import logger


def parametrizeData():
    return [(1)]


@allure.title("To verify that status code is 200 for update posts service")
@pytest.mark.parametrize("id", parametrizeData())
def test_put_update_posts_status_code(id):
    try:
        # Calling the update_posts service and validating status code is 200
        response = put_update_post_service.update_new_post(id)
        log_response_data.from_reponse('update_posts', response)
        assert response.status_code == 200
        logger.error('test_put_update_posts_status_code is Passed')
    except Exception as e:
        # In case any exception marking teh test case as Failed
        logger.error('test_put_update_posts_status_code is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


@allure.title("To verify the schema for update posts service")
@pytest.mark.parametrize("id", parametrizeData())
def test_put_update_posts_schema_valid(id):
    # Calling the update_posts service and validating schema for the service
    response = put_update_post_service.update_new_post(id)
    log_response_data.from_reponse('update_posts', response)
    schema = put_update_posts_service_schema.schema
    try:
        schema.validate(response.json())
        assert True
        logger.info('test_put_update_posts_schema_valid is Passed')
    except Exception as e:
        # In case any exception, marking the test case as Failed
        logger.error(f'test_put_update_posts_schema_valid is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


@allure.title("To verify verify the record updated for update posts service")
@pytest.mark.parametrize("id", parametrizeData())
def test_put_update_posts_verify_record(id):
    try:
        # Calling the update_posts and validating against get_one_posts_service
        put_response = put_update_post_service.update_new_post(id)
        log_response_data.from_reponse('update_posts', put_response)
        put_response_id = put_response.json()['id']
        get_response = get_one_posts_service.get_post_by_id(id)
        log_response_data.from_reponse('get_one_posts', get_response)
        get_title = get_response.json()['title']
        get_body = get_response.json()['body']
        d = {'id': put_response_id}
        data = json.loads(read_json.readfile("update_post.json", d))
        data_title = data['title']
        data_body = data['body']

        assert get_title == data_title
        assert get_body == data_body
        logger.info('test_put_update_posts_verify_record is Passed')
    except Exception as e:
        # In case any exception, marking the test case as Failed
        logger.error(f'test_put_update_posts_verify_record is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e
