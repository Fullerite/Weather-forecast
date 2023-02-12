from api_call import get_forecast, get_sunrise_sunset
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    city = request.values.get('city')
    weather = get_forecast(city)
    dates_unique = set()
    if city is None or weather['cod'] == '404':
        return render_template('index-default.html')
    else:
        for timestamp in weather['list']:
            dates_unique.add(timestamp['dt_txt'][:10])
        dates_unique = sorted(list(dates_unique))

        sun_time_first_day = get_sunrise_sunset(weather['city']['coord']['lat'],
                                                weather['city']['coord']['lon'],
                                                dates_unique[0])
        sun_time_second_day = get_sunrise_sunset(weather['city']['coord']['lat'],
                                                 weather['city']['coord']['lon'],
                                                 dates_unique[1])
        sun_time = [sun_time_first_day, sun_time_second_day]

        return render_template('index.html',
                               city=city,
                               weather=weather,
                               dates_unique=dates_unique,
                               sun_time=sun_time)


if __name__ == '__main__':
    app.run()
