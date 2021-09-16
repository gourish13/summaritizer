"""
Controller for post activities
"""

from datetime import datetime, timedelta
from uuid import uuid4

from app.models.summaritizer_model import (
    add_post,
    get_post,
    remove_post,
    update_post_content,
)
from app.utils.email import send_email
from app.utils.hash import hashed
from app.utils.keygen import genkey
from app.consts.envs import BASE_URL


def new_post(author, hrs, mins, email, content):
    deletes_at = datetime.utcnow() + timedelta(hours = hrs, minutes = mins)
    _uuid = str(uuid4())
    key = genkey()
    _id = add_post(_uuid, author, deletes_at, email, content, hashed(key))
    send_email(email, BASE_URL, _id, _uuid, key, hrs, mins)
    return dict(id = f'{_id}-{_uuid}')


def show_post(_id, _uuid):
    deletes_at = datetime.utcnow()
    return get_post(_id, _uuid, deletes_at)


def delete_post(_id, _uuid, key):
    deletes_at = datetime.utcnow()
    return remove_post(_id, _uuid, key, deletes_at)


def update_post(_id, _uuid, author, content, key):
    deletes_at = datetime.utcnow()
    return update_post_content(_id, _uuid, author, 
                               content, key, deletes_at)
