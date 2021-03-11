"""
Summaritizer database model
"""

from pydal import Field

from .connect import db

db.define_table('summary',
                Field('uuid', type='string', unique=True, required=True, notnull=True),
                Field('author', type='string', length=30, required=True, notnull=True),
                Field('delete_at', type='datetime', required=True, notnull=True),
                Field('email', type='string', required=True, notnull=True),
                Field('content', type='text', required=True, notnull=True),
                Field('key', type='string', required=True, notnull=True)
                )

summary_delete_expired_query = """
CREATE OR REPLACE FUNCTION summary_delete_expired_rows() RETURNS TRIGGER
    LANGUAGE plpgsql
    AS $$
BEGIN
    DELETE FROM summary WHERE delete_at < NOW();
    RETURN NEW;
END;
$$;
"""

trigger_query = """
DROP TRIGGER IF EXISTS summary_delete_expired_rows_trigger ON summary;
CREATE TRIGGER summary_delete_expired_rows_trigger
    AFTER INSERT OR UPDATE ON summary
    EXECUTE PROCEDURE summary_delete_expired_rows();
"""

db.executesql(summary_delete_expired_query)
db.executesql(trigger_query)

db.commit()


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


def get_post(_id, _uuid):
    result = db.summary(
        (db.summary.id == _id) & (db.summary.uuid == _uuid)
    )
    if not result:
        return result.first().as_dict()
    return None


def remove_post(_id, _uuid, key):
    modified = db.summary(
        (db.summary.id == _id) & (db.summary.uuid == _uuid) & (db.summary.key == key)
    ).delete()
    db.commit()
    return modified


def update_post(_id, _uuid, author, content, key):
    modified = db.summary(
        (db.summary.id == _id) & (db.summary.uuid == _uuid) & (db.summary.key == key)
    ).update(author = author, content = content)
    db.commit()
    return modified
