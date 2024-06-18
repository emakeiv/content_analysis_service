from fastapi import FastAPI
from endpoints import records, statistics

def create_server():
    server = FastAPI(debug=True)
    server.include_router(records.router)
    server.include_router(statistics.router)
    return server


app = create_server()