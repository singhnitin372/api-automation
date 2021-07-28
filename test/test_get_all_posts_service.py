from request import get_all_posts_service
import allure
from schemas import get_all_posts_service_schema
from utility import log_response_data
from utility.log import logger


@allure.title("To verify status code is 200 for get all posts service")
def test_get_all_post_status_codes():
    try:
        response = get_all_posts_service.get_request()
        log_response_data.from_reponse('get_all_posts', response)
        assert response.status_code == 200
        logger.info('test_get_all_post_status_codes is Passed')
    except Exception as e:
        logger.error(f'test_get_all_post_status_codes is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


@allure.title("To verify get all posts service return more than 100 records")
def test_get_all_post_records():
    try:
        response = get_all_posts_service.get_request()
        log_response_data.from_reponse('get_all_posts', response)
        assert len(response.json()) > 99
        logger.info(f'test_get_all_post_records is Passed')
    except Exception as e:
        logger.error(f'test_get_all_post_records is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e


@allure.title("To verify schema for get all posts service")
def test_get_all_post_verify_schema():
    try:
        response = get_all_posts_service.get_request()
        log_response_data.from_reponse('get_all_posts', response)
        schema = get_all_posts_service_schema.schema
        try:
            schema.validate(response.json())
            assert True
            logger.error(f'test_get_all_post_verify_schema is Passed')
        except Exception as e:
            logger.error(f'test_get_all_post_verify_schema is Failed')
            assert False, e
    except Exception as e:
        logger.error(f'test_get_all_post_verify_schema is Failed')
        logger.error(f'Error message is: {e}')
        assert False, e
