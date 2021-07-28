from request import get_invalid_posts_service
import allure
from utility import log_response_data
from utility.log import logger


@allure.title("To verify that status code is 404 for invalid posts service")
def test_get_invalid_posts_status_codes():
    try:
        # Calling the invalid posts service
        response = get_invalid_posts_service.get_invalid_post()
        # logging the service response in logger
        log_response_data.from_reponse('get_invalid_posts', response)
        # Checking for the assertion
        assert response.status_code == 404
        logger.info("test_get_invalid_posts_status_codes is Passed")
    except Exception as e:
        # In case an exception, mark the test case as failed
        logger.error("test_get_invalid_posts_status_codes is Failed")
        logger.error(f"Error message is : {e}")
        assert False, e
