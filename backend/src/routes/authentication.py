from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException

from fastapi.param_functions import Body
from ..controller.authentication_controller import AuthenticationController

authentication_router = APIRouter(prefix="/auth", tags=["Authentication"])
authentication_controller = AuthenticationController()

# NOTE:// Must upgrade to HTTPS for this password exchange to be secure
@authentication_router.post("/login")
async def post_login(username = Body(...), password = Body(...)):
    result = authentication_controller.post_login(username, password)
    if result == None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    return result

@authentication_router.post("/signup")
async def post_signup(username = Body(...), email = Body(...), password = Body(...)):
    result = authentication_controller.post_signup(username, email, password)
    if result == None:
        raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED, detail="Unable to create new user")
    return result
