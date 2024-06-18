from fastapi import APIRouter

router = APIRouter()

@router.get("/records")
async def get_records():
    return {"message": "I will return all records"}