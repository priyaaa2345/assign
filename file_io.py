# created for file I/O exception

import logging


logging.basicConfig(
    filename="file_io",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

print("you cant access me")

print("Oopss..u did it")
