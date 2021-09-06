"""
Summaritizer database model
"""

from app.utils.hash import verify
from .summaritizer_schema import db

def add_post(_uuid, author, deletes_at, email, content, key):
    _id = db.summary.insert(
            uuid = _uuid,
            author = author,
            delete_at = deletes_at,
            email = email,
            content = content,
            key = key
    )
    db.commit()
    return _id


def get_post(_id, _uuid, deletes_at):
    result = db(
        (db.summary.id == _id) & 
        (db.summary.uuid == _uuid) &
        (db.summary.delete_at > deletes_at)
    ).select(db.summary.author, db.summary.content)
    if result:
        return result.first().as_dict()
    return {'status': 'no post found'}


def match_key(_id, _uuid, deletes_at, key):
    result = db(
        (db.summary.id == _id) &
        (db.summary.uuid == _uuid) &
        (db.summary.delete_at > deletes_at)
    ).select(db.summary.key)
    if result:
        verify(key, result.first().as_dict().get('key'))
    else:
        return None


def remove_post(_id, _uuid, key, deletes_at):
    key_status = match_key(_id, _uuid, deletes_at, key)
    if key_status == None:
        return {
            'status': '''\
Post has already expired \
and has been deleted. \
The one you are seeing is \
a local cached version.'''}
    if key_status == False:
        return {'status': 'Key does not match'}
    db(
        (db.summary.id == _id) & 
        (db.summary.uuid == _uuid)
    ).delete()
    db.commit()
    return {'status': 'Post deleted'}


def update_post_content(
    _id, _uuid, author, content, key, deletes_at):
    key_status = match_key(_id, _uuid, deletes_at, key)
    if key_status == None:
        return {
            'status': '''\
Post has already expired \
and has been deleted. \
The one you are seeing is \
a local cached version.'''}
    if key_status == False:
        return {'status': 'Key does not match'}
    db(
        (db.summary.id == _id) & 
        (db.summary.uuid == _uuid)
    ).update(author = author, content = content)
    db.commit()
    return {'status': 'Post updated'}
