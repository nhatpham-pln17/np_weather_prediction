from src.const.global_map import RESOURCE_MAP


def weather_predict_func(
    precipitation: float,
    wind_speed: float,
    temperature_avg: float,
) -> str:

    input = [precipitation, wind_speed, temperature_avg]
    input = RESOURCE_MAP["data_pipeline"].transform([input])

    result = RESOURCE_MAP["model"].predict(input)

    if result == 0:
        return "drizzle"
    elif result == 1:
        return "fog"
    elif result == 2:
        return "rain"
    elif result == 3:
        return "snow"
    elif result == 4:
        return "sun"
