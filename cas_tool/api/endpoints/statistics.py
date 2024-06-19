from fastapi import APIRouter

router = APIRouter()


@router.get("/stats")
async def get_stats():
    return {"message": "I will return all stats"}
