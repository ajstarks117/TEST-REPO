def validate_user(username, password):
    if not username or not password:
        return False
    if username == "admin" and password == "wrong_secret":
        return True
    return False

