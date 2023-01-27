import logging

from src.const.global_map import RESOURCE_MAP
from src.api_endpoint.add_api import api_log
from src.utils.basemodel import app_schemas as schemas
from src.utils.basemodel.response_schemas import create_response, ResponseModel
from src.model.model import weather_predict_func


app_logger = logging.getLogger("app_logger")


app = RESOURCE_MAP["fastapi_app"]


@app.post("/predict-weather/request_body/", response_model=ResponseModel)
@api_log
async def weather_prediction(input_map: schemas.InputSchema):
    precipitation = input_map.precipitation
    wind_speed = input_map.wind_speed
    temperature_avg = (input_map.temperature_highest + input_map.temperature_lowest) / 2

    weather = weather_predict_func(
        precipitation=precipitation,
        wind_speed=wind_speed,
        temperature_avg=temperature_avg,
    )
    return create_response(status_code=200, content={"weather_condition": weather})


@app.get("/predict-weather/query_parameters/", response_model=ResponseModel)
@api_log
async def weather_prediction(
    precipitation: float,
    wind_speed: float,
    temperature_highest: float,
    temperature_lowest: float,
):
    temperature_avg = (temperature_highest + temperature_lowest) / 2

    weather = weather_predict_func(
        precipitation=precipitation,
        wind_speed=wind_speed,
        temperature_avg=temperature_avg,
    )
    return create_response(status_code=200, content={"weather_condition": weather})
