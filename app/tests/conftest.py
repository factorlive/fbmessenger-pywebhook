import pytest


@pytest.fixture(scope=module)
def message_header() -> :
    h = fixtures / 'header_w_attach.json'
    with open(h, 'r') as f:
        header = json.load(f)