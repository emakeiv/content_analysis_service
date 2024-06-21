from typing import List
from api.schemas.model import TvShow
from sal.ops import services, uows
from fastapi import APIRouter, HTTPException


router = APIRouter()


@router.get("/records/")
async def get_records():
    try:
        records = services.get_records(uows.SqlUnitOfWork())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return records


@router.get("/record/{record_id}")
async def get_record(record_id: int):
    return {"message": f"I will return record {record_id}"}


@router.post("/record/", response_model=TvShow, status_code=201)
async def add_record(record: TvShow):
    try:
        services.save_record(record, uows.SqlUnitOfWork())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return record
