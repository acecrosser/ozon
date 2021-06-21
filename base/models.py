from cursor import cursor
from datetime import datetime


def put_url(ids: str, url: str):
    cursor.execute(
        "INSERT INTO short (token, url, date) "
        f"({ids}, {url}, {datetime.now()}"
    )


def get_url(colum: str, type: str, key: str):
    cursor.execute(
        f"SELECT {colum} FROM short "
        f"WHERE {type} LIKE '{key}'"
    )
    return cursor.fetchone()

