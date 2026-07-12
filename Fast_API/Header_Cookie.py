from fastapi import FastAPI , Header, Cookie

app = FastAPI()

@app.get("/home")
def home(user_agent: str = Header()):
    return {
        "browser": user_agent
    }
@app.get("/id")
def profile (username: str = Cookie()):
    return {
        "user": username
    }


