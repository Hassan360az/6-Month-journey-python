from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login/")
def user_data(name: str = Form(...), password: str = Form (...)):
    return {
        "name", name ,"Success"
    }

