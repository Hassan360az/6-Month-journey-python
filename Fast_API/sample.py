from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login/")
def login_user(username: str = Form(...), password: str = Form(...)):
    return {"user": username, "status": "Success"}": username, "status": "Logged In!"}