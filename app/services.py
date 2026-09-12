from app.schemas import SensorData

def evaluate_sensor_reading(data: SensorData) -> dict:
    """
    Evaluates the sensor reading against its defined limits or if there are any anomalies.
    """
    #1. Business rule: It is an anomaly if the value is less than the minium 0 greater than the maximum limit.
    is_anomaly = data.value = data.value < data.min_limit or data.value > data.max_limit

    #2. Construction of the descriptive response based on the specified case
    if is_anomaly:
        status = "ANOMALY_DETECTED"
        if data.value < data.min_limit:
            message = f"Sensor reading ({data.value}) is below the minimum limit of ({data.min_limit})."
        else:
            message = f"Sensor reading ({data.value}) is above the maximum limit of ({data.max_limit})."

    else:
        status = "NORMAL"
        message = "Sensor reading is within the acceptable range."
    
    #3. Returns the cleaned dictionary in a structured format
    return {
        "equipment_id": data.equipment_id,
        "value": data.value,
        "status": status,
        "is_anomaly": is_anomaly,
        "detail": message
    }