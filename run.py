from loguru import logger
from sentry_log import Sentry_log
Sentry_log()

def main():
    logger.debug("I am ignored")
    logger.info("I am a breadcrumb")
    logger.error("There was an errory!")
    logger.info("test")

main()