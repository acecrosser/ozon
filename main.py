import os
from fastapi import FastAPI, HTTPException
from starlette.routing import compile_path
from base.models import get_url, put_url, Item
from tools import resize_link, check_link
from urllib.parse import urlparse


app = FastAPI(title='API Short Link. (TestTask)')


@app.post('/short/')
def get_short_url(item: Item):
    if check_link(item.url):
        token = resize_link(item.url)
        put_url(token, item.url)
        short_url = ''.join((os.getenv('SHORT_URL'), token))
        return {'url': short_url }
    raise HTTPException(400, 'Bad link send')


@app.post('/long/')
def get_long_url(item: Item):
    if check_link(item.url):
        token = urlparse(item.url).path[1:] # remove the extra slash
        long_url = get_url('url', 'token', token)
        return {'url': long_url[0]}
    raise HTTPException(400, 'Bad link send')
