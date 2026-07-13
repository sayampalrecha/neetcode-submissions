import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values(by='recordDate')

    weather['prev_temp'] = weather['temperature'].shift(1)
    weather['prev_date'] = weather['recordDate'].shift(1)

    condition = (weather['temperature']>weather['prev_temp']) & \
                ((weather['recordDate'] - weather['prev_date'])==pd.Timedelta(days=1))
    
    return weather[condition][['id']]
