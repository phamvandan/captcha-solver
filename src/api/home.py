from fastapi import  Form, UploadFile
from fastapi import APIRouter

router = APIRouter()
import json
from starlette.responses import FileResponse
from services.run_brute_force import *

router = APIRouter(
    prefix="",
    tags=["home"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/run-brute-force")
def run_brute_force(
    login_url: str = Form(...),
    form_tag: str = Form(...),
    captcha_failure_text: str = Form(...),
    user_pass_wrong_text: str = Form(...),
    post_data: str = Form(...),
    id: str = Form(...),
    username_file: UploadFile = Form(...),
    password_file: UploadFile = Form(...),
):
    post_data = json.loads(post_data)
    # read file content
    with username_file.file as file:
        usernames = [line.strip() for line in file]
    with password_file.file as file:
        passwords = [line.strip() for line in file]

    # run brute-force
    do_run_brute_force(login_url, form_tag, captcha_failure_text, user_pass_wrong_text, post_data, usernames, passwords, id)

    # Example response:
    return {
        "message": "Finish",
    }

@router.get("/status-brute-force/{id}")
def get_status_brute_force(id: str):
    records = ["null"]
    records = do_get_run_brute_force_by_id(id)
    if len(records)==0:
        return "null"
    print("records", records[0])
    return records[0]

# Serve the index.html file
@router.get("/")
async def index():
    return FileResponse("static/index.html")