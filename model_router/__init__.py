import sys, os
from pydantic import BaseModel
from typing import Any, Mapping, Sequence, Union, List

import inspect
import os, sys
from fastapi.openapi.docs import get_swagger_ui_html

class ImageResponse(BaseModel):
    code: int = 0
    data: List[str] = []
    message: str = ""


# FastAPI的一些函数
def get_function_default_args(func):
    '''获取函数默认参数'''
    sign = inspect.signature(func)
    return {
        k: v.default
        for k, v in sign.parameters.items()
        if v.default is not inspect.Parameter.empty
    }

def swagger_monkey_patch(*args, **kwargs):
    """
    Wrap the function which is generating the HTML for the /docs endpoint and
    overwrite the default values for the swagger js and css.
    """
    param_dict = get_function_default_args(get_swagger_ui_html)
    swagger_js_url = param_dict['swagger_js_url'].replace('https://cdn.jsdelivr.net/npm/', 'https://unpkg.com/')
    swagger_css_url = param_dict['swagger_css_url'].replace('https://cdn.jsdelivr.net/npm/', 'https://unpkg.com/')
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url=swagger_js_url,
        swagger_css_url=swagger_css_url
    )


