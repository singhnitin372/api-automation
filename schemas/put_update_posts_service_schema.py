from schema import Schema

from utility.log import logger

# schema for update_posts service
schema = Schema(
    {
        "id": int
    }
)

logger.info("Service name is: update_posts")
logger.info(f"Schema for service is: {str(schema)}")
