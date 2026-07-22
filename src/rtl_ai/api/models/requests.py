from pydantic import BaseModel
class AnalysisRequest(BaseModel):
 issue:str
 context:str=''
