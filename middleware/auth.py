from fastapi import HTTPException, Request
from firebase_admin import auth

async def firebase_auth_middleware(request: Request,call_next):
    # Check if request is authorized with Firebase ID token
    authorization = request.headers.get("Authorization")
    if not authorization or not authorization.startswith("Bearer "):
        # Check if "__session" cookie is present
        if not request.cookies or "__session" not in request.cookies:
            raise HTTPException(status_code=403, detail="Unauthorized")

    id_token = None
    if authorization and authorization.startswith("Bearer "):
        # Read the ID Token from the Authorization header
        id_token = authorization.split("Bearer ")[1]
    elif request.cookies and "__session" in request.cookies:
        # Read the ID Token from the "__session" cookie
        id_token = request.cookies["__session"]

    if not id_token:
        raise HTTPException(status_code=403, detail="Unauthorized")

    try:
        # Verify the Firebase ID token
        decoded_id_token = auth.verify_id_token(id_token)
        return decoded_id_token
    except auth.InvalidIdTokenError:
        raise HTTPException(status_code=403, detail="Unauthorized")
    except auth.ExpiredIdTokenError:
        raise HTTPException(status_code=403, detail="Unauthorized")
