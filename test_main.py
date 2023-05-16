from urlshort import create_app
from confteste import client, app

def test_shorten(client):
    response = client.get('/')
    assert b'Shortenz' in response.data