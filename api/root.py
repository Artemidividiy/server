from fastapi import FastAPI
def api_main():
    app = FastAPI()
    @app.get("/root")
    async def root(): 
        return "this is a root"



