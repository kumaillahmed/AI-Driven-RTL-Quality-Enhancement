from pydantic import BaseModel

class AnalysisRequest(BaseModel):
    log:str

class AnalysisResponse(BaseModel):
    summary:str
    root_cause:str
