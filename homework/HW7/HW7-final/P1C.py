from Markov import Markov

city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}

city_weather_result = city_weather.copy()
print("\n")
predictions = {}
for city, weather in city_weather_result.items():
    weather_today = Markov(day_zero_weather = weather)
    weather_today.load_data()
    pred_weather = weather_today.get_weather_for_day(7, 100)

    counter = {}

    for pred in pred_weather:
        if pred not in counter:
            counter[pred] = 1
        else:
            counter[pred] += 1

    city_weather_result[city] = counter

    print(f"{city}: {counter}.")

print("\n")
print("Most likely weather in seven days")
print("----------------------------------")

for city, preds in city_weather_result.items():
    sol = max(preds, key=preds.get)
    print(f"{city}: {sol}")

print("\n")
