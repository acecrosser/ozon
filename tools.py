from random import randint
from urllib.parse import urlparse
from hashids import Hashids


def check_link(link:str) -> bool:
    link = urlparse(link)
    if link.scheme and link.netloc:
        return True
    return False


def resize_link(link: str):
    long_link = urlparse(link)
    # generator = [randint(1, 11) for x in range(1, 5)]
    hashids = Hashids(salt=f'{long_link.path}')
    ids = hashids.encode(1, 3, 5, 7)
    return ids