
from fastapi import FastAPI, Request
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from routers import sign_in, sign_up, menu, me
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



app = FastAPI()

app.mount("/static", StaticFiles(directory="/home/n_kratos/send_messages/frontend/"), name="public")
templates = Jinja2Templates(directory="/home/n_kratos/send_messages/frontend")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(sign_in.router)
app.include_router(sign_up.router)
app.include_router(menu.router)
app.include_router(me.router)


@app.get("/", tags=["root"], summary="Acceuil")
async def acc(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=1600, log_level="info", workers= 10, reload = True)