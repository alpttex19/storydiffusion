import os
import shutil
import uuid

from fastapi import UploadFile


def split_type_file_url(url: str):
    x = url.split("user_id=")[1]
    user_id = x.split("&")[0]
    filename = x.split("&")[1].replace("filename=", "")
    type = x.split("&")[2].replace("type=", "")

    return user_id, filename, type

def split_task_file_url(url: str):
    x = url.split("task_id=")[1]
    task_id = x.split("&")[0]
    filename = x.split("&")[1].replace("filename=", "")

    return task_id, filename


def get_type_file_url(user_id: str, filename: str, fileType: str):
    print(user_id,filename,fileType)
    url_format = 'https://u447318-aeda-ad4cafe6.bjc1.seetacloud.com:8443/file_model/get_user_type_file_from_url?user_id={user_id}&filename={filename}&type={type}'
    return url_format.format(user_id=user_id, type=fileType, filename=filename)


def get_task_file_url(task_id: str, filename: str):
    url_format = 'https://u447318-aeda-ad4cafe6.bjc1.seetacloud.com:8443/file_model/get_task_file_from_url?task_id={task_id}&filename={filename}'
    return url_format.format(task_id=task_id, filename=filename)


def uploadFile(file: UploadFile, user_id: str, fileType: str):
    save_path_format = '/root/autodl-tmp/story_data/user/{user_id}/{type}/'
    save_path = save_path_format.format(user_id=user_id, type=fileType)

    suffix = file.filename.split('.')[-1]

    os.makedirs(os.path.join(save_path), exist_ok=True)

    while True:
        unique_id = uuid.uuid4()
        path = os.path.join(save_path, f"{fileType}_{unique_id}.{suffix}")
        if not os.path.exists(path):
            break
    filename = f"{fileType}_{unique_id}.{suffix}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return get_type_file_url(user_id, filename, fileType)
