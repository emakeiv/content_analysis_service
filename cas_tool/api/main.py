from fastapi import FastAPI
from api.endpoints import records, statistics
from dal.orm.mapper import start_mappers


def create_server():
    server = FastAPI(debug=True)
    server.include_router(records.router)
    server.include_router(statistics.router)
    return server


start_mappers()
app = create_server()
