from fastapi import FastAPI
app = FastAPI(title="SentinelX API Gateway", version="0.1.0")
@app.get("/health")
def health():
    return {"status":"ok","response_mode":"simulation"}
