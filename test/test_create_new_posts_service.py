from request import post_create_posts_service, get_one_posts_service
from schemas import create_new_posts_service_schema
from utility import read_json, log_response_data
import json
import allure

from utility.log import logger


@allure.title("To verify create posts service status code is 201")
def test_create_posts_status_code():
    try:
        # calling the create_posts_service
        response = post_create_posts_service.create_new_post()
        # logging the response in logger.
        log_response_data.from_reponse('create_posts_service', response)
        # asserting the status code is 200
        assert response.status_code == 201
        # marking pass in the logger
        logger.info("test_create_posts_status_code is Passed")
    except Exception as e:
        # Incase any exception marking the test case as failed
        logger.error(f'test_create_posts_status_code is Failed')
        logger.error(f'Error is: {e}')
        assert False, e


@allure.title("To verify schema for create posts service")
def test_create_posts_schema_verify():
    # calling the create_posts_service
    response = post_create_posts_service.create_new_post()
    # logging the response in logger
    log_response_data.from_reponse('create_posts_service', response)
    # getting the schema for create_posts_service
    schema = create_new_posts_service_schema.schema
    try:
        # validating the schema
        schema.validate(response.json())
        logger.info(f"test_create_posts_schema_verify is Passed")
        assert True
    except Exception as e:
        # In case schema validation failed, marking it as failed
        logger.error(f'test_create_posts_schema_verify is Failed')
        logger.error(f'Error is: {e}')
        assert False, e


@allure.title("To verify record created for create posts service ")
def test_create_new_post_verify_post_created():
    try:
        # calling the create_posts_service
        response = post_create_posts_service.create_new_post()
        # logging the response data in logger
        log_response_data.from_reponse('create_posts_service', response)
        # extracting the id
        id = response.json()['id']
        # calling the get one post service by id
        get_response = get_one_posts_service.get_post_by_id(id)
        # logging the data for get one post service by id
        log_response_data.from_reponse('get_one_posts_service', get_response)
        if get_response.status_code == 200:
            # Assert the post and get api request and response body data for validation
            get_title = get_response.json()['title']
            get_body = get_response.json()['body']
            data = json.loads(read_json.readfile("create_new_post.json"))
            post_title = data['title']
            post_body = data['body']

            assert post_body == get_body
            assert post_title == get_title
            logger.info(f'test_create_new_post_verify_post_created is Passed')
        else:
            # if get_one_posts_service response is other than 200 for newly created id, then mark test case as failed
            logger.error(f'test_create_new_post_verify_post_created is Failed')
            assert False, 'Record not updated for the post service'
    except Exception as e:
        # In case any exception, mark the test case as failed and logged the exception
        logger.error(f'test_create_new_post_verify_post_created is Failed')
        logger.error(f'Error is: {e}')
        assert False, e
