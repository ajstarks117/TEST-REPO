from auth import validate_user

def auth_middleware(request):
    auth_header = request.get('headers', {}).get('Authorization', '')
    if not auth_header.startswith('Bearer '):
        return False
    try:
        credentials = auth_header.split(' ')[1]
        username, password = credentials.split(':')
        return validate_user(username, password)
    except Exception:
        return False

