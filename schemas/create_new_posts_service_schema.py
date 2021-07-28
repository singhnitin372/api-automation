from schema import Schema

from utility.log import logger

# Schema for create_new_post service
schema = Schema(
    {
        "id": int
    }
)

logger.info("Service name is: create_new_post")
logger.info(f"Schema for service is: {str(schema)}")
