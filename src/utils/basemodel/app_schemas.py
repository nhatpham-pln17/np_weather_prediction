from pydantic import BaseModel


class InputSchema(BaseModel):
    session: str
    precipitation: float
    wind_speed: float
    temperature_highest: float
    temperature_lowest: float
