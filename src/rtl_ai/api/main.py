from fastapi import FastAPI
from .routes.analysis import router
app=FastAPI(title='RTL AI API')
app.include_router(router)
@app.get('/health')
def health(): return {'status':'ok'}
