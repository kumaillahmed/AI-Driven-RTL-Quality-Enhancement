from pydantic import BaseModel
class AnalysisResponse(BaseModel):
 summary:str
 recommendation:str
