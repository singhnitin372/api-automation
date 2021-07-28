from schema import Schema

from utility.log import logger

# schema for get_one_posts service
schema = Schema(

    {
        "userId": int,
        "id": int,
        "title": str,
        "body": str
    }
)
logger.info("Service name is: get_one_posts")
logger.info(f"Schema for service is: {str(schema)}")
