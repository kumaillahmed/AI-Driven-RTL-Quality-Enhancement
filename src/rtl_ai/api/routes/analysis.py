from fastapi import APIRouter
from rtl_ai.api.models.schemas import AnalysisRequest, AnalysisResponse

router=APIRouter(prefix="/analysis",tags=["Analysis"])

@router.post("/",response_model=AnalysisResponse)
def analyze(req:AnalysisRequest):
    return AnalysisResponse(
        summary="Placeholder analysis",
        root_cause="Placeholder root cause"
    )
