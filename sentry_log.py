import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
import logging
from sentry_sdk import set_tag
from loguru import logger

class Sentry_log:

    def __init__(self) -> None:
        logging.basicConfig(level=logging.DEBUG)

        sentry_logging = LoggingIntegration(
            level=logging.DEBUG,  # Capture info and above as breadcrumbs
            event_level=logging.DEBUG  # Send errors as events
        )
        
        sentry_sdk.init(
            dsn="https://371b5a0238e51da1a65703a12c4e6f16@o4507634027855872.ingest.us.sentry.io/4507634031460352",
            traces_sample_rate=1.0,
            profiles_sample_rate=1.0,
            integrations=[sentry_logging]
        )
        
        logger.add(self.sentry_handler, level="DEBUG")

    def sentry_handler(self, message):
        record = message.record
        print(message.record)
        set_tag("QUEUE", "queue - name")
        custom_metrics = "FUNCTION_NAME | SCRAPER_QUEUE | FILE_NAME |"
        custom_metrics = custom_metrics.replace("FILE_NAME", record['file'].name)
        custom_metrics = custom_metrics.replace("FUNCTION_NAME", record['function'])

        event_data = {
            "message": f"{record['message']} | {custom_metrics}",
            "level": record["level"].name.lower(),  # Convert log level to lowercase
            "extra": {
                "custom_data": "Additional context or data can go here",
                "metrics": custom_metrics  # Include custom metrics in extra data
            }
        }
        sentry_sdk.capture_event(event_data)


