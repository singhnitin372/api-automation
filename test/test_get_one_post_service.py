import allure
import pytest
from request import get_one_posts_service
from schemas import get_one_posts_service_schema
from utility import log_response_data
from utility.log import logger


def parametrizeData():
    return [(1)]


@allure.title("To verify that status code is 200 for get post service")
@pytest.mark.parametrize("id", parametrizeData())
def test_get_one_post_status_codes(id):
    try:
        # calling the get_one_posts service and validating status codes is 200
        response = get_one_posts_service.get_post_by_id(id)
        log_response_data.from_reponse('get_one_posts', response)
        assert response.status_code == 200
        logger.info('test_get_one_post_status_codes is Passed')
    except Exception as e:
        # Mark fail in case any Exception
        logger.error('test_get_one_post_status_codes is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


@allure.title("To verify get one post service returns only one record ")
@pytest.mark.parametrize("id", parametrizeData())
def test_get_one_post_records(id):
    try:
        # calling the get_one_posts service and validating api returns only one record
        response = get_one_posts_service.get_post_by_id(id)
        log_response_data.from_reponse('get_one_posts', response)
        assert response.json()['id'] == id
        logger.info('test_get_one_post_records is Passed')
    except Exception as e:
        # Mark fail in case any Exception
        logger.error('test_get_one_post_records is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


@allure.title("To verify schema for get one post service")
@pytest.mark.parametrize("id", parametrizeData())
def test_get_one_post_verify_schema(id):
    # calling the get_one_posts service and validating the schema of api
    response = get_one_posts_service.get_post_by_id(id)
    log_response_data.from_reponse('get_one_posts', response)
    schema = get_one_posts_service_schema.schema
    try:
        schema.validate(response.json())
        assert True
        logger.info('test_get_one_post_verify_schema is Passed')
    except Exception as e:
        # Mark fail in case any Exception
        logger.error('test_get_one_post_verify_schema is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


@allure.title("To verify get one post service id in response matches the input (1)")
@pytest.mark.parametrize("id", parametrizeData())
def test_get_one_post_response_matches_input(id):
    try:
        # calling the get_one_posts service and validating the id
        response = get_one_posts_service.get_post_by_id(id)
        log_response_data.from_reponse('get_one_posts', response)
        assert response.json()['id'] == id
        logger.info('test_get_one_post_response_matches_input is Passed')
    except Exception as e:
        # Mark fail in case any Exception
        logger.error("test_get_one_post_response_matches_input is Failed")
        logger.error(f'Error message is: {e}')
        assert False, e
