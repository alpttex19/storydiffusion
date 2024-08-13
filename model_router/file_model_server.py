import os
import shutil
import uuid

from fastapi import APIRouter, UploadFile, File, requests
from fastapi.responses import FileResponse
from pydantic import BaseModel
from starlette.responses import StreamingResponse

from model_router import fileModel as fileModel

router = APIRouter(prefix="/file_model",
                   tags=["file_model"],
                   dependencies=[],
                   responses={404: {"description": "Not found"}}, )


class Response(BaseModel):
    code: int = 0
    message: str = ""
    data: str = ""


@router.get("/get_task_file_from_url")
async def text2text_splitshot(task_id: str, filename: str):
    task_path = "/root/autodl-tmp/story_data/storage/tasks/"

    filepath = task_path + task_id + "/" + filename

    return FileResponse(filepath)


@router.get("/get_user_type_file_from_url")
async def text2text_splitshot(user_id: str, filename: str, type: str):
    save_path_format = '/root/autodl-tmp/story_data/user/{user_id}/{type}/'
    save_path = save_path_format.format(user_id=user_id, type=type) + filename
    return FileResponse(save_path)




@router.post("/uploadFile")
async def updateFile(user_id: str, type: str, file: UploadFile):
    url = fileModel.uploadFile(file, user_id, type)
    response = Response()
    response.data = url
    response.code = 200
    response.message = "success"
    return response
