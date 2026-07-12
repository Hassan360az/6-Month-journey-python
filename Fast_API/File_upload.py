from fastapi import FastAPI , UploadFile

app = FastAPI()

@app.post("/upload")
def upload (file: UploadFile):
    return {
        "File_Name": file.filename
    }
    