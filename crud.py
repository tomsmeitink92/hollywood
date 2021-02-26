import warnings
import sqlalchemy.exc
from contextlib import contextmanager
from config import session


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    try:
        yield session
        session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        session.rollback()
        if "psycopg2.errors.UniqueViolation" in f"{e}":
            warnings.warn(f"{e}")
        else:
            raise
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
