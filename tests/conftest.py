import os
import tempfile

import pytest

from proximalog import create_app
from proximalog.db import get_db, init_db


with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf-8')


@pytest.fixture()
def app():
    # Create and open a temporary file,
    # Returning the file object and the path to it.
    db_fd, db_path = tempfile.mkstemp()
    print(db_fd, db_path)

    app = create_app({
        'TESTING': True,  # tell Flask that the app is in test mode.
        'DATABASE': db_path,  # overriding db path so it points to temporary path instead of the instance folder
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
