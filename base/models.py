from .cursor import cursor
from main import HTTPException
from datetime import datetime
from pydantic import BaseModel
from psycopg2.errors import UniqueViolation


class Item(BaseModel):
    url: str


def put_url(token: str, url: str):
    try:
        cursor.execute(
            "INSERT INTO short (token, url, date) "
            f"VALUES ('{token}', '{url}', '{datetime.now()}')"
        )
    except UniqueViolation as err:
        pass


def get_url(colum: str, type: str, key: str):
    cursor.execute(
        f"SELECT {colum} FROM short "
        f"WHERE {type} LIKE '{key}'"
    )
    item = cursor.fetchone()
    if not item:
        raise HTTPException(400, 'Link not found')
    return item
