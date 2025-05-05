import logging

# logging.basicConfig(level=logging.INFO)
# logging.info("This is info ")
#
logging.basicConfig(level=logging.CRITICAL)
logging.critical("This is info ")

print('Here')
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",  # Save to file
    filemode="w"         # Overwrite file on each run
)

logging.debug("This is a debug message (used for tracing)")
logging.info("This is an info message (general updates)")
logging.warning("This is a warning message (something's not right)")
logging.error("This is an error message (an error occurred)")
logging.critical("This is a critical message (something crashed)")
import os
print("Logging to:", os.getcwd())


def divide(a, b):
    import pdb; pdb.set_trace()
    return a / b

divide(10, 2)
