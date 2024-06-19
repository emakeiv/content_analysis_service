from typing import List
from sal.ops import services
from dal.model import TvShow
from fastapi import APIRouter, HTTPException
from dal.repos.RecordsRepository import RecordsRepository


router = APIRouter()

@router.get("/records/", response_model=List[TvShow])
async def get_records()
    repo = RecordsRepository(session)
    records = repo.list()
    return records

@router.get("/records/{record_id}", response_model=TvShow)
async def get_record(record_id: int):
    repo = RecordsRepository(session)
    record = repo.get(record_id)
    if record is None:
        raise HTTPException(status_code=404, detail="record not found")
    return record

@router.post("/records/", response_model=str)
async def add_record(record: TvShow):
    try:
        repo = RecordsRepository(session)
        response = services.store_record(record, repo, session)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  