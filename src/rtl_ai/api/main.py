from fastapi import FastAPI
from rtl_ai.api.routes.analysis import router as analysis_router

app = FastAPI(
    title="RTL AI API",
    description="API for AI-driven RTL Quality Enhancement",
    version="1.0.0"
)
app.include_router(analysis_router)

@app.get("/")
def root():
    return {"status":"ok","service":"RTL AI API"}
