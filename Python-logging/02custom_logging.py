import logging
import os

# try:
#     logging.basicConfig(level=logging.INFO, filename="log_folder/log.log", filemode="w",
#     format = "%(asctime)s - %(levelname)s - %(message)s")
# except FileNotFoundError as err:
#     os.mkdir("log_folder")
#     logging.basicConfig(level=logging.INFO, filename="log_folder/log.log", filemode="w",
#     format = "%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("log_folder/custom_log.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


logger.info("Testing new log")

try: 
    1 / 0
except ZeroDivisionError:
    logger.exception("ZeroDivisionError")