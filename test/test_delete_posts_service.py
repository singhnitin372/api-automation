import pytest
from request import delete_post_service, get_one_posts_service
import allure

from utility import log_response_data
from utility.log import logger


# Parametrize the test data
def parametrizeData():
    return [(1)]


@allure.title("To verify the delete posts service status code is 200")
@pytest.mark.parametrize("id", parametrizeData())
def test_delete_posts_status_code(id):
    try:
        # Calling delete_post_service by passing an id
        response = delete_post_service.delete_post(id)
        # log the response data for the api
        log_response_data.from_reponse('delete_post', response)
        # Check for status code 200
        assert response.status_code == 200
        # Log the pass result
        logger.info("test_delete_posts_status_code is Passed")
    except Exception as e:
        # Mark the test case fail in case any Exception and log the whole details
        logger.error(f'test_delete_posts_status_code is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


@allure.title("To verify delete posts service record ")
@pytest.mark.parametrize("id", parametrizeData())
def test_delete_posts_verify_data(id):
    try:
        # Calling delete_post_service by passing an id
        response = delete_post_service.delete_post(id)
        # log the response data for the api
        log_response_data.from_reponse('delete_post', response)
        # Check for deleted id by calling the get single post service
        get_response = get_one_posts_service.get_post_by_id(id)
        # As for perfect delete id should not be present and we would get 404 error
        if get_response.status_code == 404:
            # if status is 404, pass the test case
            logger.info("test_delete_posts_verify_data is Passed")
            assert True
        else:
            # if status is not 404, fail the test case
            logger.error(f'test_delete_posts_verify_data is Failed')
            assert False, "Delete operation failed"
    except Exception as e:
        # Mark the test case failed in case any Exception and log the whole details
        logger.error(f'test_delete_posts_verify_data is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e
