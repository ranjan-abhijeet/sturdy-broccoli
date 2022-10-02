import logging
import os

# setting logging configuration
try:
    logging.basicConfig(level=logging.INFO, filename="log_folder/log.log", filemode="w", 
    format="%(asctime)s - %(levelname)s - %(message)s")
except FileNotFoundError:
    os.makedir("log_folder")
    logging.basicConfig(level=logging.INFO, filename="log_folder/log.log", filemode="w", 
    format="%(asctime)s - %(levelname)s - %(message)s")

# logging info
ALGORITHM = "SHA256"
logging.info(f"the value of variable ALGORITHM is {ALGORITHM}")

# logging error
try: 
    1/0
except ZeroDivisionError as err:
    logging.error("ZeroDivisionError", exc_info=True)

try: 
    float("adjaks")
except ValueError as err:
    logging.exception("ValueError")
