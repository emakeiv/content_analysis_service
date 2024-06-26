from typing import List
from uuid import uuid4, UUID
from api.schemas.model import TvShowRecordSchema, TVShowRecordsListSchema
from sal.db_ops import services, uows
from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.get("/records/", response_model=TVShowRecordsListSchema)
async def get_records():
    try:
        records = services.get_records(0, 10, uows.DatabaseUnitOfWork())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"records": records}


@router.get("/record/{record_id}", response_model=TvShowRecordSchema)
async def get_record(record_id: int):
    return {"message": f"I will return record {record_id}"}


@router.post("/record/")
async def add_record(record: TvShowRecordSchema):
    try:
        record.id = uuid4()
        record = services.save_record(record.model_dump(), uows.DatabaseUnitOfWork())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return record
