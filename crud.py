from contextlib import contextmanager
from config import session


@contextmanager
def session_scope():
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()