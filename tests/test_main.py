from fastapi.testclient import TestClient
from app.main import app
from app.services import evaluate_sensor_reading
from app.schemas import SensorData

# Create a TestClient instance for testing the FastAPI app
client = TestClient(app)

#---------------------------------------------------------------
# 1. Unit Tests (services.py)
#---------------------------------------------------------------

def test_evaluate_sensor_reading_normal():
    """Verify that a normal sensor reading returns status 'NORMAL'"""
    sensor_input = SensorData(
        equipment_id="DEV-100",
        value=25.0,
        min_limit=10.0,
        max_limit=30.0
    )
    result = evaluate_sensor_reading(sensor_input)
    assert result["status"] == "NORMAL"
    assert result["is_anomaly"] is False

def test_evaluate_sensor_reading_anomaly_high():
    """Verify that a valor above the maximum limit returns status 'ANOMALY_DETECTED'"""
    sensor_input = SensorData(
        equipment_id="DEV-100",
        value=50.0,
        min_limit=10.0,
        max_limit=30.0
    )
    result = evaluate_sensor_reading(sensor_input)
    assert result["status"] == "ANOMALY_DETECTED"
    assert result["is_anomaly"] is True

#---------------------------------------------------------------
# 2. Integration Tests (Endpoints HTTP)
#---------------------------------------------------------------

def test_health_check_endpoint():
    """Verify that the /health check endpoint returns HTTP 200"""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Service is running"}

def test_validate_endpoint_success():
    """Verify the response HTTP the endpoint POST /validate"""
    payload = {
        "equipment_id": "DEV-200",
        "value": 15.0,
        "min_limit": 5.0,
        "max_limit": 25.0
    }
    response = client.post("/api/v1/validate", json=payload)
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["status"] == "NORMAL"
    assert data["is_anomaly"] is False

#---------------------------------------------------------------
# 3. Tests the case limit and errors (Validation Errors)
#---------------------------------------------------------------

def test_validate_endpoint_missing_field():
    """ Verify thaht send an imcoplete JSON returns HTTP 422 (Unprocessable Entity)"""
    payload = {
        "equipment_id": "DEV-300",
        #Intentionally missing 'value', 'min_limit', and 'max_limit'
    }
    response = client.post("/api/v1/validate", json=payload)
    assert response.status_code == 422

def test_validate_endpoint_invalid_data_type():
    """Verify that sending an invalid data type returns HTTP 422 (Unprocessable Entity)"""
    payload = {
        "equipment_id": "DEV-400",
        "value": "invalid_string",  # Invalid data type for 'value'
        "min_limit": 5.0,
        "max_limit": 25.0
    }
    response = client.post("/api/v1/validate", json=payload)
    assert response.status_code == 422