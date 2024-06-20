from typing import List
from api.schemas.model import TvShow
from sal.ops import services, uows
from fastapi import APIRouter, HTTPException


router = APIRouter()


@router.get("/records/", response_model=List[TvShow])
async def get_records():
    return {"message": "I will return all records"}


@router.get("/record/{record_id}", response_model=TvShow)
async def get_record(record_id: int):
    return {"message": f"I will return record {record_id}"}


@router.post("/record/")
async def add_record(record: TvShow):
    try:
        services.store_record(record, uows.SqlUnitOfWork())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
