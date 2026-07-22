from fastapi import APIRouter
from ..models.requests import AnalysisRequest
from ..models.responses import AnalysisResponse
router=APIRouter(prefix='/analysis',tags=['analysis'])
@router.post('/',response_model=AnalysisResponse)
def analyze(req:AnalysisRequest):
 return AnalysisResponse(summary=f'Received issue: {req.issue}',recommendation='Connect parser, ML, RAG and LLM pipeline.')
