
from model_router import swagger_monkey_patch



from fastapi import FastAPI, applications
applications.get_swagger_ui_html  = swagger_monkey_patch
app = FastAPI()

from model_router import storydiffusion, file_model_server
app.include_router(storydiffusion.router)
app.include_router(file_model_server.router)


# 之后可以使用
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=6006)
