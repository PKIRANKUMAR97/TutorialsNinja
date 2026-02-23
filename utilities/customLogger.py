import logging
import os

class LogGen:

    @staticmethod
    def loggen():

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        path = os.path.join(os.getcwd(), "logs", "automation.log")

        file_handler = logging.FileHandler(path)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            "%m/%d/%Y %I:%M:%S %p"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        if not logger.handlers:
            logger.addHandler(file_handler)

        return logger