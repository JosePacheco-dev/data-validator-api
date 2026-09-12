from pydantic import BaseModel, Field

class SensorData(BaseModel):
    equipment_id: str =  Field(
        ...,
        description="Unique identifier for the equipment",
        json_schema_extra={"example": "DEV-001"}
    )
    value: float = Field(
        ...,
        description="The sensor reading value",
        json_schema_extra={"example": 24.5}
    )
    min_limit: float = Field(
        ...,
        description="The minimum acceptable limit for the sensor reading",
        json_schema_extra={"example": 10.0}
    )
    max_limit: float = Field(
        ...,
        description="The maximum acceptable limit for the sensor reading",
        json_schema_extra={"example": 30.0}
    )    