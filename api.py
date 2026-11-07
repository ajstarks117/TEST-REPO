from auth import validate_user

def login_endpoint(request_data):
    if "username" not in request_data or "password" not in request_data:
        return {"status": 400, "message": "Missing credentials"}
    if validate_user(request_data["username"], request_data["password"]):
        return {"status": 200, "message": "Success"}
    else:
        return {"status": 401, "message": "Unauthorized"}
