"""
Summaritizer database schema
"""

from pydal import Field

from .connect import db

db.define_table(
                    'summary',
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
    AS 
$$
BEGIN
    DELETE FROM summary WHERE delete_at <= NOW();
    RETURN NEW;
END;
$$;
"""

trigger_query = """
DROP TRIGGER IF EXISTS summary_delete_expired_rows_trigger ON summary;
CREATE TRIGGER summary_delete_expired_rows_trigger
    BEFORE INSERT OR UPDATE ON summary
    EXECUTE PROCEDURE summary_delete_expired_rows();
"""

create_index = "CREATE INDEX IF NOT EXISTS idx_summary ON summary(id, uuid) INCLUDE (key, author, content);"

db.executesql(summary_delete_expired_query)
db.executesql(trigger_query)
db.executesql(create_index)

db.commit()
