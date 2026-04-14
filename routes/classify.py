from fastapi import APIRouter, Query, HTTPException
from starlette import status

from services.genderize import fetch_gender
from utils.helperMethods import compute_confidence, get_timestamp

router = APIRouter()

@router.get("/classify")
async def classify(name: str = Query(None)):
    if not name or name.strip() == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"status": "error", "message": "Missing or empty name parameter"})

    data = await fetch_gender(name)

    if data.get("gender") is None or data.get("count",0) == 0:
        raise HTTPException(status_code=422, detail={"status": "error", "message": "No prediction available for the provided name"})

    probability = data["probability"]
    sample_size = data["count"]

    return {"status": "success",
            "data":{
                "name": data["name"],
                "gender": data["gender"],
                "probability": probability,
                "sample_size": sample_size,
                "is_confident" : compute_confidence(probability, sample_size),
                "processed_at" : get_timestamp()
            }}