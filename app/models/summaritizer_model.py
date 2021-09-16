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
        return { 
            'data': result.first().as_dict(),
            'status_code': 200
        }
    return {
        'data': 'no post found',
        'status_code': 404
    }


def match_key(_id, _uuid, deletes_at, key):
    result = db(
        (db.summary.id == _id) &
        (db.summary.uuid == _uuid) &
        (db.summary.delete_at > deletes_at)
    ).select(db.summary.key)
    if result:
        return verify(key, result.first().as_dict().get('key'))
    else:
        return None


def remove_post(_id, _uuid, key, deletes_at):
    key_status = match_key(_id, _uuid, deletes_at, key)
    if key_status == None:
        return {
            'data': '''\
Post has already expired \
and has been deleted. \
The one you are seeing is \
a local cached version.''',
            'status_code': 406
        }
    if key_status == False:
        return {
            'data': 'Key does not match',
            'status_code': 403
        }
    db(
        (db.summary.id == _id) & 
        (db.summary.uuid == _uuid)
    ).delete()
    db.commit()
    return {
        'data': 'Post successfully deleted',
        'status_code': 200
    }


def update_post_content(
    _id, _uuid, author, content, key, deletes_at):
    key_status = match_key(_id, _uuid, deletes_at, key)
    if key_status == None:
        return {
            'data': '''\
Post has already expired \
and has been deleted. \
The one you are seeing is \
a local cached version.''',
            'status_code': 406
        }
    if key_status == False:
        return {
            'data': 'Key does not match',
            'status_code': 403
        }
    db(
        (db.summary.id == _id) & 
        (db.summary.uuid == _uuid)
    ).update(author = author, content = content)
    db.commit()
    return {
        'data': 'Post successfully updated',
        'status_code': 201
    }
