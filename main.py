from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def root():
    return {"Mensagem":"Deu certo"}
#teste1