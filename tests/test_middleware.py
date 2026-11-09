from middleware import auth_middleware

def test_middleware_success():
    assert auth_middleware({"headers": {"Authorization": "Basic admin:secret"}}) is True

def test_middleware_failure():
    assert auth_middleware({"headers": {"Authorization": "Basic admin:wrong"}}) is False


def test_null_authorization_header():
    assert auth_middleware({'headers': {'Authorization': None}}) is False
