"""There’s not much to test about the factory itself. Most of the code will be executed for each test already,
so if something fails the other tests will notice.

The only behavior that can change is passing test config.
If config is not passed, there should be some default configuration,
otherwise the configuration should be overridden."""

from proximalog import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_running(client):
    response = client.get('/running')
    print(response.data)
    assert response.data == b'Hi! I am in proximalog up and running...'

