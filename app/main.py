from fastapi import FastAPI
from app.schemas import SensorData
from app.services import evaluate_sensor_reading

app = FastAPI(
    title="Data Validator & Anomaly API",
    description="This API validates sensor data and detects anomalies in the data.",
    version="1.0.0",
)

@app.get("/api/v1/health")
def health_check():
    return { "status": "ok", "message": "Service is running" }

@app.post("/api/v1/validate")
def validate_sensor_data(data: SensorData):
    """
    Endpoint to validate sensor data and detect anomalies.
    """
    result = evaluate_sensor_reading(data)
    return{
        "code": 200,
        "data": result,
    }