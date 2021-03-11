"""
Controller for post activities
"""

from datetime import datetime, timedelta
from uuid import uuid4

from app.models.summaritizer_model import (
    add_post,
    get_post,
    remove_post,
    update_post,
)
from app.utils.email import send_email
from app.utils.hash import hashed
from app.utils.keygen import genkey
from app.consts.envs import BASE_URL


def new_post(author, hrs, mins, email, content):
    deletes_at = datetime.now() + timedelta(hours = hrs, minutes = mins)
    _uuid = str(uuid4())
    key = genkey()
    _id = add_post(_uuid, author, deletes_at, email, content, hashed(key))
    send_email(email, BASE_URL, _id, _uuid, key)
    return dict(id = _id, uuid = _uuid)


def show_post(_id, _uuid):
    result = get_post(_id, _uuid)
    if not result:
        return {'author': ''}
    return result


def delete_post(_id, _uuid, key):
    status = remove_post(_id, _uuid, hashed(key))
    return {'status': 'ok'} if status else {'status': '!ok'}

def update_post(_id, _uuid, author, content, key):
    status = update_post(_id, _uuid, author, content, hashed(key))
    return {'status': 'ok'} if status else {'status': '!ok'}
