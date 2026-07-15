import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)

logging.info("Program Started")
logging.debug("Debugging Code")
logging.warning("This is a Warning.")
logging.error("This is an error message.")