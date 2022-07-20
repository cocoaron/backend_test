# install fastapi, uvicorn, sqlalchemy, pymysql

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from typing import List
from starlette.middleware.cors import CORSMiddleware

import time

from db import session
from model import UserTable, user

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins = ["*"],
	allow_credentials = True,
	allow_methods = ["*"],
	allow_headers = ["*"],
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
def hello_world():
	print("This page contains no message, will redirect")
	time.sleep(5)
	response = RedirectResponse(url='/main')
	return response
	# return {"This is a home page, move to http://127.0.0.1/main"}

@app.get("/main", response_class=HTMLResponse)
async def main(request: Request):
	return templates.TemplateResponse("interest.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
	return templates.TemplateResponse("login.html", {"request": request})

@app.get("/ranking", response_class=HTMLResponse)
async def ranking(request: Request):
	return templates.TemplateResponse("ranking.html", {"request": request})

@app.get("/search", response_class=HTMLResponse)
async def search(request: Request):
	return templates.TemplateResponse("login.html", {"request": request})

@app.get("/signup", response_class=HTMLResponse)
async def signup(request: Request):
	return templates.TemplateResponse("signup.html", {"request": request})

@app.get("/userinfo", response_class=HTMLResponse)
async def userinfo(request: Request):
	return templates.TemplateResponse("userinfo.html", {"request": request})

'''
@app.get("/userinfo/{id}", response_class=HTMLResponse)
async def userinfo(request: Request, id: str):
	return templates.TemplateResponse("userinfo.html", {"request": request, "id":id})
'''

@app.get("/users")
def read_users():

	users = session.query(UserTable).all()

	return users

@app.get("/users/{user_id}")
def read_user(user_id: int):

	user = session.query(UserTable).filter(UserTable.id == user_id).first()

	return user

@app.post("/users")
def create_user(name: str, age: int):

	user = UserTable()
	user.name = name
	user.age = age

	session.add(user)
	session.commit()

	return f"{name} has been created."

@app.put("/users")
def update_users(users: List[user]):

	for i in users:
		user = session.query(UserTable).filter(UserTable.id == i.id).first()
		user.name = i.name
		user.age = i.age

	return f"{i.name} has been updated."

@app.delete("/users")
def delete_users(user_id: int):

	user = session.query(UserTable).filter(UserTable.id == user_id).delete()
	session.commit()

	return read_users
